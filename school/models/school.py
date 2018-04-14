from django.db import models

# Completed 
# no one
class SchoolModel(models.Model):
    name = models.CharField(max_length=200, null=False)
    logo_image = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    email = models.EmailField(null=True)
    phone = models.BigIntegerField(null=False)
    code = models.CharField(max_length=10, null=False)

    class Meta:
        unique_together = ('name', 'code')

    def __str__(self):
        return self.name

