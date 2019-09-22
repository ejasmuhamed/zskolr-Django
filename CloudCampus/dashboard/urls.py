from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('academic/', views.academic_year, name='academic_year'),
    path('academic/new', views.academic_new, name='academic_new'),

    path('course/', views.course_list, name='course_list'),
    path('course/new', views.course_new, name='course_new'),

    path('subject/', views.subject_list, name='subject_list'),
    path('subject/new', views.subject_new, name='subject_new'),

    path('semester/', views.semester_list, name='semester_list'),
    path('semester/new', views.semester_new, name='semester_new'),

    path('attendence/', views.attendence_select, name='attendence_select'),
    path('attendence/mark', views.attendence_mark, name='attendence_mark'),
    path('attendence/view', views.attendence_view, name='attendence_view'),

    path('student/profile/select/', views.student_select, name='student_select'),
    path('student/profile/view/', views.student_profile, name='student_profile'),
    url(r'^student/profile/view/(?P<pk>\d+)/$', views.student_profile_roll, name='student_profile_roll'),
    url(r'^student/profile/edit/(?P<pk>\d+)/$', views.student_profile_edit, name='student_profile_edit'),
    path('student/profile/add/', views.student_profile_add, name='student_profile_add'),
    path('profile/', views.my_profile, name='my_profile'),

    path('notification/view/', views.notification_view, name = 'notification_view'),
    url(r'^notification/edit/(?P<pk>\d+)/$', views.notification_edit, name='notification_edit'),
    path('notification/add/', views.notification_add, name = 'notification_add'),
    path('notification/student/view/', views.notification_student_view, name = 'notification_student_view'),
    url(r'^notification/student/edit/(?P<pk>\d+)/$', views.notification_student_edit, name='notification_student_edit'),
    path('notification/student/add/', views.notification_student_add, name = 'notification_student_add'),

    path('seminar/add/', views.seminar_add, name = 'seminar_add'),
    #url(r'^seminar/view/(?P<pk>\d+)/$', views.seminar_add, name='seminar_add'),

    path('assignment/add/', views.assignment_add, name = 'assignment_add'),


    path('project/add/', views.project_add, name = 'project_add'),
    #url(r'^assignment/view/(?P<pk>\d+)/$', views.assignment_view, name='assignment_view'),

    path('teacher/profile/add', views.teacher_profile_add, name = 'teacher_profile_add'),


    path('uploads/view/', views.view_uploads, name = 'view_uploads'),
    #url(r'^project/view/(?P<pk>\d+)/$', views.project_view, name='project_view'),
    ]