import pytest
from django.urls import reverse
from django.test import Client


@pytest.fixture
def resp(client: Client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200
