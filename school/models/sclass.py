from django.db import models
from django.utils import timezone
from .school import SchoolModel

# Completed
# Admin get, post, update
class ClassModel(models.Model):
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=5, null=False)
    section = models.CharField(max_length=2, null=False)

    class Meta:
        unique_together = ('name', 'section', 'school')

    def __str__(self):
        return str(self.name) + " (" + str(self.section)+ ")"
