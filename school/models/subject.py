from django.db import models
from .school import SchoolModel

# Completed
class SubjectModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=50, null=False)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('code', 'school')
    def __str__(self):
        return str(self.name) + "(" + str(self.code) + ")" 


