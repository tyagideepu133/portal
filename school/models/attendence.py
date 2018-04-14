from django.db import models

from .session import StudentSessionModel


# Student get(self)
# Teacher get(all), post(self)
# Admin delete, upadate, get(all)
class StudentAttendenceModel(models.Model):
    student = models.ForeignKey(to=StudentSessionModel, on_delete=models.CASCADE)
    attended = models.BooleanField(null=False)
    date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return str(self.student) + " " + str(self.date) 