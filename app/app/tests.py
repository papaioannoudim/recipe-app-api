from django.test import TestCase
from app.calc import add, subtract


class CaclTests(TestCase):

    def test_add_numbers(self):
        # Test that two numbers are added together
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        # Test that values are subtracted and returned
        self.assertEqual(subtract(6, 11), 5)


# Notes:
# docker-compose run app sh -c "python manage.py test"
# docker-compose run app sh -c "python manage.py test && flake8"
# docker-compose build
