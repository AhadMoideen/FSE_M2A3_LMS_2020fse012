# Create your views here.

from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from notification_service.models import Notification
from notification_service.serializers import NotificationSerializer


class UserNotificationAPIView(APIView):

    def post(self, request, email):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data.__setitem__('hasRead', True)
            serializer.save()
        send_mail('FSE-LMS: Registration Successful', 'Welcome to FSE, hope to be at service.',
                  'ahadmoideen@gmail.com', [request.data['recipient']])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        print('Get all notifications.')
        try:
            notifications = Notification.objects.all()
        except Notification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def delete(self, request):
        Notification.objects.all().delete()
        return Response({})

class CourseNotificationAPIView(APIView):
    def post(self, request, courseId):
        recipients = request.data['recipients']
        if request.data['type'] == 'NEW_EVAL':
            for recipient in recipients:
                notificationSerializer = NotificationSerializer(data={'recipient':recipient, 'type':'NEW_EVAL','hasRead':False})
                if notificationSerializer.is_valid():
                    notificationSerializer.save()
            send_mail('FSE-LMS: New evaluation',
                      'New evaluation ('+ str(request.data['evaluationType']) +') has been added to ' + str(request.data['courseName']),
                      'ahadmoideen@gmail.com',
                      recipients)
        elif request.data['type'] == 'NEW_COURSE':
            for recipient in recipients:
                notificationSerializer = NotificationSerializer(
                    data={'recipient': recipient, 'type': 'NEW_COURSE', 'hasRead': False})
                if notificationSerializer.is_valid():
                    notificationSerializer.save()
            send_mail('FSE-LMS: New course:'+str(request.data['courseName']), 'You have been added to: ' + str(request.data['courseName']),
                      'ahadmoideen@gmail.com', recipients)
        return Response({}, status=status.HTTP_201_CREATED)