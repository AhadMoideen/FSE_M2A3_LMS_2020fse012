from django.urls import path

from .views import UserNotificationAPIView, CourseNotificationAPIView

urlpatterns = [
    path('notification/', UserNotificationAPIView.as_view()),
    path('notification/user/<str:email>', UserNotificationAPIView.as_view()),
    path('notification/course/<str:courseId>', CourseNotificationAPIView.as_view()),
    path('notification/course/<str:courseId>/e-val', CourseNotificationAPIView.as_view())
]
