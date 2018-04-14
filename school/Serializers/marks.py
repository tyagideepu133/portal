from rest_framework import serializers
from ..models.marks import ExamModel, SubjectMarkModel, StudentMarksModel

class ExamModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(ExamModelSerializer, self).__init__(*args, **kwargs)
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
        model = ExamModel
        fields = '__all__'

class SubjectMarkSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(SubjectMarkSerializer, self).__init__(*args, **kwargs)
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
        model = SubjectMarkModel
        fields = '__all__'

class StudentMarksModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(StudentMarksModelSerializer, self).__init__(*args, **kwargs)
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
        model = StudentMarksModel
        fields = '__all__'