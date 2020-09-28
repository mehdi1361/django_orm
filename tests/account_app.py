import importlib
from django.conf import settings
from django.test import Client


def test_blog_module_exists():
    assert importlib.util.find_spec("account") is not None


def test_blog_on_install_apps():
    assert "account.apps.AccountConfig" in settings.INSTALLED_APPS


def test_login_admin():
    c = Client()
    response = c.get("/admin/account/profile/")
    assert response.status_code != 404
