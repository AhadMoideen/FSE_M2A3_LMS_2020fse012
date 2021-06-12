from django.test import TestCase
from rest_framework import status


class RegisterTestCases(TestCase):
    def setUp(self):
        self.payload = {
            "dob": "2021-01-26T10:51:35.915Z",
            "fullName": "Student God",
            "password": "123456",
            "userName": "ahad@tripworld.com",
            "userType": "FACULTY"
        }
        self.payloadNegativeName = {
            "dob": "2021-01-26T10:51:35.915Z",
            "fullName": "",
            "password": "123456",
            "userName": "ahad@tripworld.com",
            "userType": "FACULTY"
        }

    def tes_registerPositive(self):
        response = self.client.post("/register/", self.payload)
        print("Status:")
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def tes_negativeName(self):
        response = self.client.post("/register/", self.payloadNegativeName)
        print("Status:")
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
