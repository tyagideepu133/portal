from rest_framework import serializers
from ..models.student import StudentModel, EnquiryModel, RegistrationModel
from ..models.auth import CustomUser, RoleModel

class StudentModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(StudentModelSerializer, self).__init__(*args, **kwargs)
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
        model = StudentModel
        fields = '__all__'

    def validate(self, data):
        if not data['id']:
            raise serializers.ValidationError("Provide CustomUserid for user")
        username = str(data['id'])
        password = data['id']
        email = ""
        if data['email'] and data['id']:
            email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        user_obj = CustomUser(username=username, email=email,
                    first_name=first_name, last_name=last_name)
        user_obj.is_active = True
        user_obj.set_password(password)
        role = RoleModel.objects.get(role="student")
        user_obj.save()
        user_obj.roles.add(role)
        data['user'] = user_obj
        return data

class EnquiryModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(EnquiryModelSerializer, self).__init__(*args, **kwargs)
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
        model = EnquiryModel
        fields = '__all__'

class RegistrationModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(RegistrationModelSerializer, self).__init__(*args, **kwargs)
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
        model = RegistrationModel
        fields = '__all__'

    