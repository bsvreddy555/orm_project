
from  django.contrib import admin
from django.urls import path
from orm_appe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home_view'),
    path('insert/',views.insert_data,name='insert_data'),
    path('delete/(?P<id>\d+)/',views.delete_view,name='delete'),
    path('update/(?P<id>\d+)/',views.update_view,name='update'),
    path('add_phone(?P<id>\d+)',views.add_phonr,name='add_phone_view'),
    path('update_phone(?P<id>\d+',views.update_phone_view,name='update_phone'),
    path('del_ph_num/(?P<id>\d+)',views.del_ph_num,name='del_ph_num'),
    path('add_course',views.Add_course,name='add_course'),
    path('user_course/(?P<id>\d+)',views.user_course_view,name='user_course'),
    path('display courses',views.display_courses,name='display_courses'),
    path('delete_stu_course/(?P<user_id>\d+)/(?P<course_id>\d+)',views.delete_student_course,name='delete_stu_course')
]