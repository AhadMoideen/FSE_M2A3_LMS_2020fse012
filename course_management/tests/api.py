from django.test import TestCase
from rest_framework import status


class LoginTestCases(TestCase):
    def setUp(self):
        self.payloadUnAuthorized = {

            "password": "123456",
            "userName": "studenta@tripworld.com",
            "userType": "STUDENT"

        }
        self.payloadBadRequest = {

            "password": "",
            "userName": "studenta@tripworld.com",
            "userType": "STUDENT"

        }

    def test_registerUnAuthorized(self):
        response = self.client.post("/login/", self.payloadUnAuthorized)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_bad_request(self):
        response = self.client.post("/login/", self.payloadBadRequest)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
