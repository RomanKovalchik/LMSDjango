from django import forms

from course.models import Course
from user.models import UserGroup
from django.urls import reverse_lazy


class GroupCourseForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True,
    )
    search = forms.CharField(widget=forms.TextInput(
        attrs={'hx-post': reverse_lazy("hx_course_search"),
               'hx-trigger': "keyup changed delay:500ms",
               'hx-target': "#search",
               'hx-swap': "outerHTML",
               'placeholder': 'Search...'})
    )

    groups = forms.ModelChoiceField(
        queryset=UserGroup.objects.all(),
        required=True,
        widget=forms.Select(attrs={'hx-post': reverse_lazy("hx_course_list"),
                                   'hx-trigger': "change",
                                   'hx-target': "#courses_list",
                                   'hx-swap': "outerHTML"})
    )

