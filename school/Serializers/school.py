from rest_framework import serializers
from ..models.school import SchoolModel

class SchoolModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(SchoolModelSerializer, self).__init__(*args, **kwargs)
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
        model = SchoolModel
        fields = '__all__'
