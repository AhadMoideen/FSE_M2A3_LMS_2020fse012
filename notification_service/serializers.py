from rest_framework import serializers

from .models import  Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['notificationId', 'recipient', 'hasRead', 'type', 'date']

