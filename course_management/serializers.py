from rest_framework import serializers

from .models import Course, Module, EvaluationComponent


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


class EvaluationComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationComponent
        fields = ['evaluationComponentId', 'marks', 'noOfQuestions', 'dateTime','type']


class CourseDetailSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=False)
    evaluationComponents = EvaluationComponentSerializer(many=True, read_only=False)

    class Meta:
        model = Course
        fields = ['courseId', 'courseName', 'description', 'faculty', 'modules', 'evaluationComponents']
