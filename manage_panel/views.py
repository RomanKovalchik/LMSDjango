from django.shortcuts import render, redirect

from course.models import Course
from manage_panel.forms import GroupCourseForm
from user.models import UserGroup


# Create your views here.
def index(request):
    form = GroupCourseForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            group = form.cleaned_data['groups']
            courses = form.cleaned_data['courses']

            group.courses.clear()
            group.courses.add(*courses)

    context = {
        'form': GroupCourseForm(initial={'courses': Course.objects.all()})
    }

    return render(request, "manage_panel/index.html", context=context)


def gr_course_form_part(request):

    if request.method == 'POST':
        context = {
            'form': GroupCourseForm(initial={'courses': UserGroup.objects.filter(id=request.POST.get('groups')).first().courses.all()})
        }
        return render(request, "manage_panel/inc/_course_list.html", context=context)
    return redirect('course_index')




