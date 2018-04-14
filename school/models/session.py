from django.db import models
from django.utils import timezone

from .staff import StaffModel
from .sclass import ClassModel
from .student import StudentModel
from .subject import SubjectModel
from .school import SchoolModel

# Completed
# Admin
class SessionModel(models.Model):
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.BooleanField(default=True)
    classes = models.ManyToManyField(ClassModel, through="ClassSessionModel")
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('start_date', 'end_date', 'school')

    def __str__(self):
        return str(self.school)+" (" + str(self.start_date) + " - " + str(self.end_date) + ") "

# Completed
# Admin
# Teacher Get
class ClassSessionModel(models.Model):
    class_id = models.ForeignKey(to=ClassModel, on_delete=models.CASCADE)
    incharge = models.ForeignKey(to=StaffModel, on_delete=models.CASCADE)
    session = models.ForeignKey(to=SessionModel, on_delete=models.CASCADE)
    students = models.ManyToManyField(StudentModel, through="StudentSessionModel")
    subjects = models.ManyToManyField(SubjectModel, through="SubjectSessionModel")

    class Meta:
        unique_together = ('class_id', 'session')

    def __str__(self):
        return str(self.class_id)

# Completed
class StudentSessionModel(models.Model):
    student = models.ForeignKey(to=StudentModel, on_delete=models.CASCADE)
    class_session = models.ForeignKey(to=ClassSessionModel, on_delete=models.CASCADE)
    enrolled_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'class_session')

    def __str__(self):
        return str(self.class_session) + " - " + str(self.student)

# Completed
# Student get
# Teacher get
# Admin 
class SubjectSessionModel(models.Model):
    subject = models.ForeignKey(to=SubjectModel, on_delete=models.CASCADE, blank=True)
    class_session = models.ForeignKey(to=ClassSessionModel, on_delete=models.CASCADE, blank=True)
    teacher = models.ForeignKey(to=StaffModel, on_delete=models.CASCADE, blank=True)

    class Meta:
        unique_together = ('subject', 'class_session', 'teacher')

    def __str__(self):
        return str(self.subject) + " (" + str(self.class_session) + ")"

#Completed
# Student(self) get
# Teacher(self) get
# Admin
class SubjectTimingModel(models.Model):
    WEEKDAYS = (('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'),
               ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'),
               ('sun', 'Sunday')
           )

    subject_session = models.ForeignKey(to=SubjectSessionModel, on_delete=models.CASCADE, blank=True)
    time = models.TimeField(blank=True)
    day = models.CharField(max_length=4, choices=WEEKDAYS, blank=True)

    class Meta:
        unique_together = ('subject_session', 'time', 'day')

    def __str__(self):
        return str(self.day) + " (" + str(self.time) + ")" + "-" + str(self.subject_session)

