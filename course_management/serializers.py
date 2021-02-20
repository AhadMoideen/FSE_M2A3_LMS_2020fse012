from rest_framework import serializers

from .models import Course, Module


class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'description', 'faculty']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['moduleId', 'name', 'description']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'description', 'faculty']


class CourseDetailSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=False)

    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'description', 'faculty', 'modules']
