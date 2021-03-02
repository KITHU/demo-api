from rest_framework.test import APITestCase
from .base_test import BaseTest
from api.src.authentication.models import User


class authentecationTestCase(BaseTest):

    def test_models_can_create_user(self):
        old_count = User.objects.count()
        self.new_user1.save()
        new_count = User.objects.count()
        self.assertEqual(new_count, old_count + 1)
