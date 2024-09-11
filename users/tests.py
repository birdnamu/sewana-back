# users/tests.py
# TDD Test Driven Development 테스트 주도 개발
# Unit Test 단위테스트를 실행할 것이다.
''' TDD 기법의 프로세스 (요약)
  1) 구현하려는 기능에 대한 테스트 코드를 작성한다.
  2) 테스트를 실행시키고, 기능이 없으니 실패한다.
  3) 테스트를 통과할 수 있는 최소한의 기능을 구현한다.
  4) 테스트를 실행시키고, 통과시키면 코드를 정리한다.
  5) 모든 기능을 구현할 때까지 이를 반복한다.
'''
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Bird

from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

class BirdModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='birdowner', password='12345')
        self.bird = Bird.objects.create(name='Tweety', owner=self.user)

    def test_bird_creation(self):
        self.assertEqual(self.bird.name, 'Tweety')
        self.assertEqual(self.bird.owner.username, 'birdowner')

    def test_bird_str(self):
        self.assertEqual(str(self.bird), 'Tweety')

class UserViewTest(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.user_data = {
      'username': 'newuser',
      'email': 'test@example.com',
      'password1': 'password123',
      'password2': 'password123',
      'fullname': 'New User'
    }
    self.response = self.client.post(reverse('user_register'), self.user_data)
