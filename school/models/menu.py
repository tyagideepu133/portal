from django.db import models
from .school import SchoolModel


class MainMenu(models.Model):
    title = models.CharField(max_length=30, null=False)
    icon = models.CharField(max_length=30, null=False)
    router_link = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.title

class SubMenu(models.Model):
    title = models.CharField(max_length=30, null=False)
    icon = models.CharField(max_length=30, null=False)
    router_link = models.CharField(max_length=30, null=False)
    menu = models.ForeignKey(MainMenu,  on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SchoolMenu(models.Model):
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)



