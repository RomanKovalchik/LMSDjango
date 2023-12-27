from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this course belongs to. A course will get all permissions granted to each of their groups.',
        related_name="custom_user_set",
        related_query_name="course",
        db_table='user_groups',
    )
    permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user_permissions',
        blank=True,
        help_text='Specific permissions for this course.',
        related_name='custom_user_set',
        related_query_name='course',
        db_table='user_permissions',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'custom_user'

    def __str__(self):
        return f'<{self.__class__.__name__}>: {self.email}'

    def __repr__(self):
        return self.__str__()


class UserGroup(models.Model):
    title = models.CharField(max_length=50)
    courses = models.ManyToManyField('course.Course', related_name='group_courses')
    users = models.ManyToManyField(CustomUser, related_name='group_users')

    def __str__(self):
        return f'<{self.__class__.__name__}>: {self.title}'

    def __repr__(self):
        return self.__str__()
