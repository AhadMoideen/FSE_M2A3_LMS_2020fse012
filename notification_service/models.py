from django.db import models


# Create your models here.
class Notification(models.Model):
    notificationId = models.AutoField(primary_key=True, editable=False)
    recipient = models.EmailField(max_length=100)
    type = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    hasRead = models.BooleanField(default=False)
