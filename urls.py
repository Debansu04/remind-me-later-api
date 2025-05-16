from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_reminder, name='create_reminder'),
    path('list/', views.list_reminders, name='list_reminders'),
]
