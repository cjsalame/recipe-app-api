from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.test', password='password123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user with an email"""
        email = "cjsalame@uc.cl"
        password = "123123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "cjsalame@UC.CL"
        user = get_user_model().objects.create_user(email, "testpass123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test email user validations"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "testpass123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        email = "cjsalame@uc.cl"
        password = "123123"
        user = get_user_model().objects.create_superuser(
            email,
            password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self. assertEqual(str(tag), tag.name)
