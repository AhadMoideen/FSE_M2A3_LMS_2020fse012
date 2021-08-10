# Create your views here.
import requests
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
        serializer = CourseRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            student_query_set = User.objects.filter(userType='STUDENT')
            if student_query_set.exists():
                serializer.validated_data.__setitem__('students', student_query_set)
            serializer.save()
            saved_course = Course.objects.get(courseId=serializer.data.get('courseId'))
            self.email_students(request, CourseDetailSerializer(saved_course).data, "NEW_COURSE")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def email_students(self, request, courseDetail, emailType):
        students = courseDetail['students']
        recipients = []
        for student in students:
            recipients.append(student['userName'])
        r = requests.post('http://localhost:7000/notification/course/' + str(courseDetail['courseId']),
                          json={
                              'courseName': str(courseDetail['courseName']),
                              'type': emailType,
                              'recipients': recipients
                          }, params=request.POST)


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
        if serializer.is_valid():
            try:
                course = Course.objects.get(courseId=courseId)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if serializer.is_valid():
                serializer.validated_data.__setitem__('course', course)
            if serializer.is_valid():
                serializer.save()
                self.email_students(request, CourseDetailSerializer(course).data, serializer.data, "NEW_EVAL")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def email_students(self, request, courseDetail, evaluationDetail, emailType):
        students = courseDetail['students']
        recipients = []
        for student in students:
            recipients.append(student['userName'])
        r = requests.post('http://localhost:7000/notification/course/' + str(courseDetail['courseId']) + '/e-val',
                          json={
                              'courseName': str(courseDetail['courseName']),
                              'type': emailType,
                              'recipients': recipients,
                              'evaluationType': str(evaluationDetail['type'])
                          }, params=request.POST)
