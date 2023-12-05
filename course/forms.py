from django import forms
from django.core.exceptions import ValidationError

from .models import Lesson


class LessonForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Введите название урока...",})
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Введите описание урока...", "class": "input-data"})
    )
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Введите текст урока...", "class": "input-data"})
    )
    activity = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Введите задание для урока...", "class": "input-data"})
    )

    class Meta:
        model = Lesson
        fields = ['title', 'description', 'text', 'activity', ]

    def clean_title(self):
        title = self.cleaned_data['title']

        if not title.startswith('ю'):
            raise ValidationError('Заголовок не начинает с ю')

        pass

        return title
