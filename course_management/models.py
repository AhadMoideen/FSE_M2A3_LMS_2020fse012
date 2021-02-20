from django.db import models
from user_management.models import User


class Course(models.Model):
    courseId = models.AutoField(primary_key=True, editable=False)
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    faculty = models.EmailField(max_length=100)
    students = models.ManyToManyField(User)


class Module(models.Model):
    moduleId = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)


class EvaluationComponent(models.Model):
    evaluationComponentId = models.AutoField(primary_key=True, editable=False)
    marks = models.IntegerField()
    noOfQuestions = models.IntegerField()
    dateTime = models.CharField(max_length=200)
    type = models.CharField(max_length=20, default='QUIZ')
    course = models.ForeignKey(Course, related_name='evaluationComponents', on_delete=models.CASCADE)
