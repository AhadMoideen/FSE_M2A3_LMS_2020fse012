# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from course_management.models import Course
from course_management.serializers import CourseSerializer, CourseRegistrationSerializer, ModuleSerializer, \
    CourseDetailSerializer, EvaluationComponentSerializer
from user_management.models import User


class CourseAPIView(APIView):

    def get(self, request, id):
        print('Course:Id:', id)
        try:
            course = Course.objects.get(courseId=id)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)

    def post(self, request):
        print('Course-Register:')
        serializer = CourseRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            studentQuerySet = User.objects.filter(userType='STUDENT')
            if studentQuerySet.exists():
                serializer.validated_data.__setitem__('students', studentQuerySet)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseUserAPIView(APIView):
    def get(self, request, email):
        print('UserId:', email)
        try:
            courses = Course.objects.filter(faculty=email)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class CourseModuleAPIView(APIView):
    def post(self, request, courseId):
        serializer = ModuleSerializer(data=request.data)
        print('Course:', courseId)
        if serializer.is_valid():
            try:
                course = Course.objects.get(courseId=courseId)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if serializer.is_valid():
                serializer.validated_data.__setitem__('course', course)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EvaluationComponentAPIView(APIView):
    def post(self, request, courseId):
        serializer = EvaluationComponentSerializer(data=request.data)
        print('Course:', courseId)
        if serializer.is_valid():
            try:
                course = Course.objects.get(courseId=courseId)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if serializer.is_valid():
                serializer.validated_data.__setitem__('course', course)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
