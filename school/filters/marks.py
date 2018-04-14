from django_filters import FilterSet, NumberFilter
from ..models.marks import ExamModel, SubjectMarkModel, StudentMarksModel


class ExamFilter(FilterSet):
    class Meta:
        model = ExamModel
        fields = ['name', 'school']

class SubjectMarkFilter(FilterSet):
    class Meta:
        model = SubjectMarkModel
        fields = [
        'exam',
        'exam__school',
        'subject_session', 
        'subject_session__subject', 
        'subject_session__class_session',
        'subject_session__teacher',
        'subject_session__class_session__incharge', 
        'subject_session__class_session__session', 
        'subject_session__class_session__session__school',
        'subject_session__class_session__class_id'
         ]


class StudentMarksFilter(FilterSet):
    class Meta:
        model = StudentMarksModel
        fields = [
            'student_session',
            'subject_marks',
            'subject_marks__exam',
            'subject_marks__exam__school',
            'subject_marks__subject_session', 
            'subject_marks__subject_session__subject', 
            'subject_marks__subject_session__class_session',
            'subject_marks__subject_session__teacher',
            'subject_marks__subject_session__class_session__incharge', 
            'subject_marks__subject_session__class_session__session', 
            'subject_marks__subject_session__class_session__session__school',
            'subject_marks__subject_session__class_session__class_id'
        ]