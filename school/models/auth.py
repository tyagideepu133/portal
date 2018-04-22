from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from .school import SchoolModel
from .security import PermissionModel

#completed
# admin
class RoleModel(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    role = models.CharField(max_length=20, null=False)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)
    permission = models.ManyToManyField(PermissionModel)

    def get_permission(self):
        return self.permission

    def __str__(self):
        return self.role

#completed
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)

# completed
# update
class CustomUser(AbstractBaseUser):
    email = models.EmailField(_('email address'))
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    first_login = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    username = models.CharField(_('username'), max_length=30, unique=True)
    roles = models.ManyToManyField(RoleModel)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def get_roles(self):
        return self.roles

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
    def is_verified(self):
        return self.verified

    def is_first_login(self):
        return self.first_login


