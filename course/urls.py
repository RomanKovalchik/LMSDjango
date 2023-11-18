from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='course_index'),
    path('<int:course_id>', views.course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>', views.lesson_card, name='lesson_card'),
]
