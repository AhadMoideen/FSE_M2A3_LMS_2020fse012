from django.urls import path

from .views import CourseAPIView, CourseUserAPIView,CourseModuleAPIView,EvaluationComponentAPIView

urlpatterns = [
    path('course/', CourseAPIView.as_view()),
    path('course/<str:id>', CourseAPIView.as_view()),
    path('course/user/<str:email>', CourseUserAPIView.as_view()),
    path('course/<str:courseId>/module', CourseModuleAPIView.as_view()),
    path('course/<str:courseId>/e-val', EvaluationComponentAPIView.as_view()),
    path('course/user/<str:email>/test', CourseUserAPIView.as_view()),
]
