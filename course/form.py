from django import forms
from django.core.exceptions import ValidationError

from .models import Lesson


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['title', 'description', 'text', 'activity',]

    def clean_title(self):
        title = self.cleaned_data['title']

        if not title.startswith('ю'):
            raise ValidationError('Заголовок не начинает с ю')

        pass

        return title


