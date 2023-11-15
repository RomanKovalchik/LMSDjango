from django.db import models

# Create your models here.


class Course(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return f'<{self.__class__.__name__}>: {self.title}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        ordering = ['id']
        db_table = 'course'