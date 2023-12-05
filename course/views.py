
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from .forms import LessonForm
from .models import Course
from .models import Lesson


# Create your views here.


#
def index(request: WSGIRequest):
    context = {
        'title': 'Main page: Courses',
        'courses': Course.objects.all(),
        'lesson': Lesson.objects.all(),
    }
    return render(request, 'course/index.html', context=context)


def course_detail(request: WSGIRequest, course_id: int):
    course = Course.objects.filter(id=course_id).first()
    if request.method == "POST":
        form = LessonForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.course = course
            form.save()

            form = LessonForm()
        else:
            pass
    else:
        form = LessonForm()


    lessons = Lesson.objects.filter(course=course).all()
    context = {
        'title': course.title,
        'course': course,
        'lessons': lessons,
        'form': form,
    }
    return render(request, 'course/detail.html', context=context)


def lesson_detail(request: WSGIRequest, course_id: int, lesson_id: int):
    lesson = Lesson.objects.filter(id=lesson_id).first()
    context = {
        'lesson': lesson,
        'course_id': course_id,
    }
    return render(request, 'course/lesson_detail.html', context=context)


