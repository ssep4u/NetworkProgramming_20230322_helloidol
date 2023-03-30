from django.urls import path

from . import views

app_name = '아이브'

urlpatterns = [
    path('원영/', views.show_원영, name='원영'),
    path('유진/', views.show_유진, name='유진'),
]