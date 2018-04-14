from rest_framework import serializers
from ..models.subject import SubjectModel

class SubjectModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        
        super(SubjectModelSerializer, self).__init__(*args, **kwargs)
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
        model = SubjectModel
        fields = '__all__'