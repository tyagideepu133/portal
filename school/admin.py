from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField
from .models.attendence import StudentAttendenceModel
from .models.marks import ExamModel, SubjectMarkModel, StudentMarksModel
from .models.student import StudentModel, EnquiryModel, RegistrationModel
from .models.staff import StaffModel
from .models.sclass import ClassModel
from .models.subject import SubjectModel
from .models.auth import  RoleModel, CustomUser
from django.conf import settings
from .models.school import SchoolModel
from .models.session import SessionModel, ClassSessionModel, StudentSessionModel, SubjectSessionModel, SubjectTimingModel
from django.contrib.auth import get_user_model
from .models.menu import MainMenu, SubMenu, SchoolMenu
from .models.security import PermissionModel
from .models.fee import FeeCategoryModel, FeeBatch, FeePayment, FeeSubCategory, FeeSubCategoryFine

MySpecialAdmin = lambda model: type('SubClass'+model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields],
    'list_select_related': [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField,))]
})


admin.site.register(CustomUser,  MySpecialAdmin(CustomUser))
admin.site.register(StudentAttendenceModel, MySpecialAdmin(StudentAttendenceModel))
admin.site.register(ExamModel, MySpecialAdmin(ExamModel))
admin.site.register(SubjectMarkModel, MySpecialAdmin(SubjectMarkModel))
admin.site.register(StudentMarksModel, MySpecialAdmin(StudentMarksModel))
admin.site.register(StudentModel, MySpecialAdmin(StudentModel))
admin.site.register(StaffModel, MySpecialAdmin(StaffModel))
admin.site.register(ClassModel, MySpecialAdmin(ClassModel))
admin.site.register(SubjectModel, MySpecialAdmin(SubjectModel))
admin.site.register(RoleModel, MySpecialAdmin(RoleModel))
admin.site.register(SchoolModel, MySpecialAdmin(SchoolModel))
admin.site.register(SessionModel, MySpecialAdmin(SessionModel))
admin.site.register(ClassSessionModel, MySpecialAdmin(ClassSessionModel))
admin.site.register(StudentSessionModel, MySpecialAdmin(StudentSessionModel))
admin.site.register(SubjectSessionModel, MySpecialAdmin(SubjectSessionModel))
admin.site.register(SubjectTimingModel, MySpecialAdmin(SubjectTimingModel))
admin.site.register(MainMenu, MySpecialAdmin(MainMenu))
admin.site.register(SubMenu, MySpecialAdmin(SubMenu))
admin.site.register(SchoolMenu, MySpecialAdmin(SchoolMenu))
admin.site.register(PermissionModel, MySpecialAdmin(PermissionModel))
admin.site.register(FeeCategoryModel, MySpecialAdmin(FeeCategoryModel))
admin.site.register(FeeSubCategory, MySpecialAdmin(FeeSubCategory))
admin.site.register(FeeSubCategoryFine, MySpecialAdmin(FeeSubCategoryFine))
admin.site.register(FeeBatch, MySpecialAdmin(FeeBatch))
admin.site.register(FeePayment, MySpecialAdmin(FeePayment))

