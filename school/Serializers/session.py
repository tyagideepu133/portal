from rest_framework import serializers
from ..models.session import SessionModel, ClassSessionModel, StudentSessionModel, SubjectSessionModel, SubjectTimingModel

class SessionModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(SessionModelSerializer, self).__init__(*args, **kwargs)
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
        model = SessionModel
        fields = '__all__'

class ClassSessionModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(ClassSessionModelSerializer, self).__init__(*args, **kwargs)
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
        model = ClassSessionModel
        fields = '__all__'

class StudentSessionModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(StudentSessionModelSerializer, self).__init__(*args, **kwargs)
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
        model = StudentSessionModel
        fields = '__all__'

class SubjectSessionModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(SubjectSessionModelSerializer, self).__init__(*args, **kwargs)
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
        model = SubjectSessionModel
        fields = '__all__'

class SubjectTimingModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(SubjectTimingModelSerializer, self).__init__(*args, **kwargs)
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
        model = SubjectTimingModel
        fields = '__all__'