
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from .models import Course
from .models import Lesson


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

def lesson_card(request: WSGIRequest, lesson_id:int):
    lesson = Lesson.objects.filter(id=1).first()
    context = {
         'title': lesson.title,
         'description':lesson.description,
         'text': lesson.text,
         'activity':lesson.activity,
         'course_id':lesson.course,
    }
    return render(request, 'course/lesson_card.html', context=context)

