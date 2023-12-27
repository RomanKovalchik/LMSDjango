from django.shortcuts import render

from manage_panel.forms import GroupCourseForm


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
        'form': GroupCourseForm()
    }

    return render(request, "manage_panel/index.html", context=context)
