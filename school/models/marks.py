from django.db import models
from .session import SubjectSessionModel, StudentSessionModel
from .school import SchoolModel


# Student get(self)
# Teacher get(self)
# Admin get, post, update
class ExamModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'school')
    def __str__(self):
        return str(self.name)


# Student get(self)
# Admin get, post, update
# Teacher post(self), get(self), update
# incharge get(self)
class SubjectMarkModel(models.Model):
    exam = models.ForeignKey(to=ExamModel, on_delete=models.CASCADE, blank=True)
    max_marks = models.IntegerField(null=False)
    pass_marks = models.IntegerField(null=False)
    subject_session = models.ForeignKey(to=SubjectSessionModel, on_delete=models.CASCADE)
    students = models.ManyToManyField(to=StudentSessionModel, through="StudentMarksModel")

    class Meta:
        unique_together = ('exam', 'subject_session', 'max_marks')
    def __str__(self):
        return str(self.subject_session) + "(" + str(self.exam) + ")"

# Student get(self)
# Admin get, post, update
# Teacher post(self), get(self), update
# incharge get(self)
class StudentMarksModel(models.Model):
    student_session = models.ForeignKey(to=StudentSessionModel, on_delete=models.CASCADE, null=True)
    subject_marks = models.ForeignKey(to=SubjectMarkModel, on_delete=models.CASCADE, null=True)
    marks = models.DecimalField(max_digits=6, decimal_places=2,null=False)

    class Meta:
        unique_together = ('student_session', 'subject_marks', 'marks')
    def __str__(self):
        return str(self.student_session)