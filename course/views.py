
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from user.models import UserGroup, CustomUser
from .forms import LessonForm
from .models import Course, UserLesson
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
    lessons = UserLesson.objects.filter(user=request.user)
    if request.method == "POST":
        form = LessonForm(request.POST)

        if form.is_valid():
            new_lesson = form.save(commit=False)
            new_lesson.course = course
            new_lesson = form.save()

            group = UserGroup.objects.filter(id=form.data.get('group')).first()
            users = CustomUser.objects.filter(group_users=group)

            new_user_lesson = [UserLesson(user=user, lesson=new_lesson) for user in users]
            UserLesson.objects.bulk_create(new_user_lesson)

            form = LessonForm()
        else:
            pass
    else:
        form = LessonForm()

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


