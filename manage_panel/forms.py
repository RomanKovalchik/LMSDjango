from django import forms

from course.models import Course
from user.models import UserGroup


class GroupCourseForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = UserGroup
        fields = ['courses', ]
