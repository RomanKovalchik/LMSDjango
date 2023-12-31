from django.db import models

from user.models import CustomUser


# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return f'<{self.__class__.__name__}>: {self.title}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'course'


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    text = models.TextField(null=True)
    activity = models.TextField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'<{self.__class__.__name__}>: {self.title}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'course_lesson'


class UserLesson(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'<{self.__class__.__name__}>: {self.user}-{self.lesson}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = 'custom_user_lesson'
