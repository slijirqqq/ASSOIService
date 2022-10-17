from rest_framework.test import APITestCase
from rest_framework import status


class APITestCaseMixin:

    def assertSuccess(self, response):
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def assertNotAuthenticated(self, response):
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class BaseAPITestCase(APITestCase, APITestCaseMixin):
    ...
