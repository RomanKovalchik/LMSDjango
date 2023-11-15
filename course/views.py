
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from .models import Course


# Create your views here.


#
def index(request: WSGIRequest):
    context = {
        'title': 'Main page: Courses',
        'courses': Course.objects.all(),
    }
    return render(request, 'course/index.html', context=context)


def course_detail(request: WSGIRequest, course_id: int):
    course = Course.objects.filter(id=course_id).first()

    context = {
        'title': course.title,
        'course': course,
    }
    return render(request, 'course/detail.html', context=context)


