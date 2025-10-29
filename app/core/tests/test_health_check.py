"""
Test for the health check API.
"""

from django.test import TestCase  # noqa
from django.urls import reverse  # noqa

from rest_framework import status  # noqa
from rest_framework.test import APIClient  # noqa


class HealthCheckTest(TestCase):
    """test health check api """

    def test_health_check(self):
        """test health check api."""
        client = APIClient()
        url = reverse('health-check')
        res = client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
