from rest_framework.test import APITestCase
from ..models import User

class authentecationTestCase(APITestCase):
    def setUp(self):
        self.new_user1 = User(
            username='james',
            email='james@yahoo.com',
            password=1234
        )

        self.new_user2 = User(
            username='njiru',
            email='njiru@hotmail.com',
            password='hot22'
        )

    def test_models_can_create_user(self):
        old_count = User.objects.count()
        self.new_user1.save()
        new_count = User.objects.count()
        self.assertEqual(new_count, old_count + 1)
