from uuid import uuid4

from django.db import models


# Create your models here.
class Course(models.Model):
    courseId = models.AutoField(primary_key=True, editable=False)
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    faculty = models.EmailField(max_length=100)
    # evaluationComponents = models.DateTimeField()
    # students = models.CharField(max_length=100)
    # modules
