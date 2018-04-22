from django.db import models
from .school import SchoolModel
from .session import SessionModel, ClassSessionModel
from .student import StudentModel
from django.utils import timezone

class FeeCategoryModel(models.Model):
    name = models.CharField(max_length=30, null=False)
    recipet_no_prefix = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class FeeSubCategory(models.Model):
    fee_category = models.ForeignKey(FeeCategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)
    amount = models.IntegerField(null=False)
    fee_type = models.CharField(max_length=30, null=False)
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class FeeSubCategoryFine(models.Model):
    fee_sub_category = models.ForeignKey(FeeCategoryModel, on_delete=models.CASCADE)
    fine_amount = models.IntegerField(null=False)
    fine_type = models.CharField(max_length=30, null=False)
    fine_increment = models.CharField(max_length=30, null=False)

    def __str__(self):
        return str(self.fee_sub_category) + " / " + str(self.fine_amount)

class FeeBatch(models.Model):
    fee_sub_category = models.ForeignKey(FeeCategoryModel, on_delete=models.CASCADE)
    fine_sub_category = models.ForeignKey(FeeSubCategoryFine, on_delete=models.CASCADE, null=True)
    class_id = models.ForeignKey(ClassSessionModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fee_sub_category) + " / " + str(self.class_id)

class FeePayment(models.Model):
    fee_sub_category = models.ForeignKey(FeeCategoryModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    fine_sub_category = models.ForeignKey(FeeSubCategoryFine, on_delete=models.CASCADE, null=True)
    fee_batch = models.ForeignKey(FeeBatch, on_delete=models.CASCADE)
    paid_at = models.DateField(null=True)
    amount_paid = models.IntegerField(null=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.fee_sub_category) + " / " + str(self.student)
