import pytest

from django.contrib.auth.models import User
from django.test import Client
pytest_mark = pytest.mark.django_db


@pytest.mark.django_db
class TestUsers:
    @staticmethod
    def create_user():
        User.objects.create_superuser(username="admin", password="1234567", is_superuser=True)

    def test_my_user(self):
        self.create_user()
        me = User.objects.get(username='admin')
        assert me.is_superuser

    def test_login_user(self):
        self.create_user()
        c = Client(HTTP_USER_AGENT='Mozilla/5.0', enforce_csrf_checks=False)
        response = c.post('/account/login/', {'username': 'admin', 'password': '1234567'})
        assert response.status_code != 404
