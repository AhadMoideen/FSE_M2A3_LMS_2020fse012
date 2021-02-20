from rest_framework import serializers

from .models import Course


class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId','courseName', 'description', 'faculty']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'description', 'faculty']
