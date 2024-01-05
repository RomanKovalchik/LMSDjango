from django import forms

from course.models import Course
from user.models import UserGroup


class GroupCourseForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True,
    )
    groups = forms.ModelChoiceField(
        queryset=UserGroup.objects.all(),
        required=True,
        widget=forms.MultipleChoiceField(attrs={"placeholder": "Введите задание для урока...", "class": "input-data"}),
    )
