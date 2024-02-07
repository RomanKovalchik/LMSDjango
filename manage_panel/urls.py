from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='panel'),
    path('hx_course_list/', views.gr_course_form_part, name='hx_course_list'),
    path('hx_course_search/', views.gr_course_form_search, name='hx_course_search'),

]
