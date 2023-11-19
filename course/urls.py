from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='course_index'),
    path('<int:course_id>', views.course_detail, name='course_detail'),
    path('<int:course_id>/<int:lesson_id>', views.lesson_detail, name='lesson_detail'),
]
