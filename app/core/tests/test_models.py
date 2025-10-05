"""
Test for model
"""
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


class ModelTest(TestCase):
    """ Test models"""
    def test_create_user_with_email_successfully(self):
        email = "testemail@example.com"
        password = "testpassword@123"

        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test1@example.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"]
        ]

        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")

            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_error(self):
        """Test creating a new user without email raises value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "sample123")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe"""
        user = get_user_model().objects.create_user(
            "test@example.com",
            "testpassword123"
        )

        recipe = models.Recipe.objects.create(
            user = user,
            title = "sample recipe name",
            time_minutes = 5,
            price = Decimal("5.50"),
            description = "sample rcipe description"
        )
        self.assertEqual(str(recipe), recipe.title)