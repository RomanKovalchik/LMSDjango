
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.db.models import Count
from django.db.models.query import QuerySet
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

    status = {str(i['is_completed']): i['total'] for i in UserLesson.objects.filter(
            lesson__in=Lesson.objects.filter(course_id=course_id),
            user=request.user
        ).values('is_completed').annotate(
            total=Count('id')
        ).order_by('is_completed')}
    progress = (status['True']/(status['False']+status['True'])) * 100

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
        'progress': progress,
    }
    return render(request, 'course/detail.html', context=context)


def lesson_detail(request: WSGIRequest, course_id: int, lesson_id: int):
    # here we should retrieve info about completed lessons
    completed_lessons = UserLesson.objects.filter(is_completed=1).count()
    total_lessons = UserLesson.objects.count()
    progress = (completed_lessons/total_lessons)*100

    lesson = Lesson.objects.filter(id=lesson_id).first()
    context = {
        'lesson': lesson,
        'course_id': course_id,
        'progress': progress,
    }
    return render(request, 'course/lesson_detail.html', context=context)


