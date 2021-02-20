from django.urls import path

from .views import CourseAPIView,CourseUserAPIView

urlpatterns = [
    path('course/', CourseAPIView.as_view()),
    path('course/<str:id>', CourseAPIView.as_view()),
    path('course/user/<str:email>', CourseUserAPIView.as_view())
]
