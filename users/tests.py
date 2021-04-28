from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
	def test_create_user(self):
		User = get_user_model()
		user = User.objects.create_user(
			username='sophia',
			email='sophiagjackson@gmail.com',
			password='Saltlife1'
		)
		self.assertEqual(user.username, 'sophia')
		self.assertEqual(user.email, 'sophiagjackson@gmail.com')
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)

	def test_create_staffuser(self):
		User = get_user_model()
		staff_user = User.objects.create_user(
			username='scott',
			email='3060marketing@gmail.com',
			password='Scott6178@',
			is_staff=True
		)
		self.assertEqual(staff_user.username, 'scott')
		self.assertEqual(staff_user.email, '3060marketing@gmail.com')
		self.assertTrue(staff_user.is_active)
		self.assertTrue(staff_user.is_staff)
		self.assertFalse(staff_user.is_superuser)

	def test_create_superuser(self):
		User = get_user_model()
		admin_user = User.objects.create_superuser(
			username='colton',
			email='coltonajackson1@gmail.com',
			password='J@cks0nc1ty'
		)
		self.assertEqual(admin_user.username, 'colton')
		self.assertEqual(admin_user.email, 'coltonajackson1@gmail.com')
		self.assertTrue(admin_user.is_active)
		self.assertTrue(admin_user.is_staff)
		self.assertTrue(admin_user.is_superuser)