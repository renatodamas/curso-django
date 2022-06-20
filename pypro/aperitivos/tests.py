import pytest
from django.urls import reverse
from django.test import Client

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client: Client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_video_title(resp):
    assert_contains(resp, '<h1>Video Aperitivo: Motivação</h1>')


def test_video_content(resp):
    assert_contains(resp, '<iframe src="https://www.youtube.com/embed/2aYplgJrPDU"')
