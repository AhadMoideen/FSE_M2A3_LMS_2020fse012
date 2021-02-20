from django.db import models


# Create your models here.


class Course(models.Model):
    courseId = models.AutoField(primary_key=True, editable=False)
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    faculty = models.EmailField(max_length=100)
    # evaluationComponents = models.DateTimeField()
    # students = models.CharField(max_length=100)


class Module(models.Model):
    moduleId = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='modules',on_delete=models.CASCADE)
