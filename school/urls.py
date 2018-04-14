from django.conf.urls import re_path, include, url
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

# # Views goes here
from .views.school import SchoolModelView
from .views.attendence import StudentAttendenceView
from .views.marks import ExamModelView, SubjectMarkView, StudentMarkView
from .views.s_class import ClassModelView
from .views.session import SessionModelView, SubjectSessionView, StudentSessionsView, ClassSessionView, SubjectTimingView
from .views.subject import SubjectModelView
from .views.auth import UserLoginAPIView
from .views.student import StudentModelView
from .views.staff import StaffModelView


attendence_router = routers.DefaultRouter()
attendence_router.register(r'student', StudentAttendenceView)

school_router = routers.DefaultRouter()
school_router.register(r'', SchoolModelView)

exam_router = routers.DefaultRouter()
exam_router.register(r'', ExamModelView)

mark_router = routers.DefaultRouter()
mark_router.register(r'subject', SubjectMarkView)
mark_router.register(r'student', StudentMarkView)

class_router = routers.DefaultRouter()
class_router.register(r'', ClassModelView)

sessions_router = routers.DefaultRouter()
sessions_router.register(r'', SessionModelView)
session_router = routers.DefaultRouter()
session_router.register(r'student', StudentSessionsView)
session_router.register(r'subject', SubjectSessionView)
session_router.register(r'class', ClassSessionView)

timing_router = routers.DefaultRouter()
timing_router.register(r'', SubjectTimingView)


subject_router = routers.DefaultRouter()
subject_router.register(r'', SubjectModelView)

student_router = routers.DefaultRouter()
student_router.register(r'', StudentModelView)

staff_router = routers.DefaultRouter()
staff_router.register(r'', StaffModelView)

urlpatterns = [
   url(r'^students/', include(student_router.urls), name='students'),
   url(r'^staffs/', include(staff_router.urls), name='staffs'),
   url(r'^sessions/', include(sessions_router.urls), name='sessions'),
   url(r'^session/', include(session_router.urls), name='session'),
   url(r'^subjects/', include(subject_router.urls), name='subjects'),
   url(r'^classes/', include(class_router.urls), name='classes'),
   url(r'^timings/', include(timing_router.urls), name='timings'),
   url(r'^attendence/', include(attendence_router.urls), name='attendence'),
   url(r'^school/', include(school_router.urls), name='school'),
   url(r'^exams/', include(exam_router.urls), name='exams'),
   url(r'^marks/', include(mark_router.urls), name='marks'),
   url(r'auth/login/', UserLoginAPIView.as_view(), name='login'),
   url(r'^docs/', include_docs_urls(title='school-api'))
]

