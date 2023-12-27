from django.shortcuts import render

from manage_panel.forms import GroupCourseForm


# Create your views here.
def index(request):


    context = {
        'form': GroupCourseForm()
    }

    return render(request, "manage_panel/index.html", context=context)