from rest_framework import serializers
from ..models.auth import CustomUser, RoleModel
from django.db.models import Q
from rest_framework_jwt.settings import api_settings

class CustomUserModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CustomUserModelSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.query_params.get('fields'):
            fields = request.query_params.get('fields')
            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {"password":{"write_only":True}}

class RoleModelModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(RoleModelModelSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.query_params.get('fields'):
            fields = request.query_params.get('fields')
            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)

    class Meta:
        model = RoleModel
        fields = '__all__'

class CustomUserLoginSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    token = serializers.CharField(allow_blank=True, read_only=True)
    id = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(label='Student Number', required=False, allow_blank=True)
    roles = RoleModelModelSerializer(many=True,  read_only=True)

    class Meta:
        model= CustomUser
        fields = [
            'username',
            'password',
            'token',
            'id',
            'roles'
        ]
        extra_kwargs = {"password":{"write_only":True}}

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data["password"]
        
        if not username:
            raise serializers.ValidationError("Username  is Required to login")
        
        user = CustomUser.objects.filter(
            Q(username=username)
        ).distinct()

        if user.exists and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("A Username is not valid")

        if user_obj:
            if not user_obj.is_active:
                raise serializers.ValidationError("Sorry you are unauthorised. Contact to admin")
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Incorrect password please try again")
            if user_obj.first_login:
                raise serializers.ValidationError("Please change password to continue further")
            if not user_obj.is_verified:
                raise serializers.ValidationError("Please wait for verifiaction")
        payload = api_settings.JWT_PAYLOAD_HANDLER(user_obj)
        data["token"] = api_settings.JWT_ENCODE_HANDLER(payload)
        data['username'] = user_obj.get_username()
        roles = user_obj.get_roles()
        roles_serializer = RoleModelModelSerializer(roles, many=True)
        print("roles:---",roles_serializer.data)
        data['roles'] = roles_serializer.data
        return data