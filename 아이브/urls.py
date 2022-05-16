from django.urls import path
from 아이브 import views

app_name = '아이브'

urlpatterns = [
    path('원영/', views.원영, name='원영'),
    path('유진/', views.유진, name='유진'),
]