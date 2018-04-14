from rest_framework import serializers
from ..models.attendence import StudentAttendenceModel

class StudentAttendenceModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(StudentAttendenceModelSerializer, self).__init__(*args, **kwargs)
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
        model = StudentAttendenceModel
        fields = '__all__'