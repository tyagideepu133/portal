from django.db import models

class PermissionModel(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return str(self.name)