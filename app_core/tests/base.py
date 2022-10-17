from rest_framework.test import APITestCase


class APITestCaseMixin:

    def assertSuccess(self, response):
        self.assertEqual(response.status_code, 200)

    def assertNotAuthenticated(self, response):
        self.assertEqual(response.status_code, 401)


class BaseAPITestCase(APITestCase, APITestCaseMixin):
    ...
