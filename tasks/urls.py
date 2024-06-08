from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.TaskListCreateAPIView.as_view()),
    path('task/<int:id>/', views.TaskDetailAPIView.as_view())
    ]


