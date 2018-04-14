from django_filters import FilterSet, NumberFilter
from ..models.session import SessionModel, ClassSessionModel, SubjectSessionModel, SubjectTimingModel, StudentSessionModel


class SessionFilter(FilterSet):
    class Meta:
        model = SessionModel
        fields = ['start_date', 'end_date', 'status', 'school']

class ClassSessionFilter(FilterSet):
    class Meta:
        model = ClassSessionModel
        fields = [
            'class_id', 'class_id__name', 'class_id__section', 'class_id__school',
            'session', 'session__school', 'session__status'
        ]

class StudentSessionFilter(FilterSet):
    class Meta:
        model = StudentSessionModel
        fields = [
            'student', 'class_session',
            'class_session__class_id', 'class_session__class_id__name', 'class_session__class_id__section', 'class_session__class_id__school',
            'class_session__session', 'class_session__session__school', 'class_session__session__status'
        ]

class SubjectSessionFilter(FilterSet):
    class Meta:
        model = SubjectSessionModel
        fields = [
            'subject','subject__school',
            'class_session', 'class_session__class_id', 'class_session__class_id__name', 
            'class_session__class_id__section', 'class_session__class_id__school',
            'class_session__session', 'class_session__session__school','class_session__session__status',
            'teacher', 'teacher__school'
        ]


class SubjectTimingFilter(FilterSet):
    class Meta:
        model = SubjectTimingModel
        fields = [
            'day', 'time', 'subject_session', 'subject_session__subject','subject_session__subject__school',
            'subject_session__class_session', 'subject_session__class_session__class_id', 'subject_session__class_session__class_id__name', 
            'subject_session__class_session__class_id__section', 'subject_session__class_session__class_id__school',
            'subject_session__class_session__session', 'subject_session__class_session__session__school','subject_session__class_session__session__status',
            'subject_session__teacher', 'subject_session__teacher__school'
        ]

