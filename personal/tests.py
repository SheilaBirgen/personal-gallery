from django.test import TestCase
from .models import Image,Location,Categories


# Create your tests here.

class TestLocation(TestCase):
    '''Test class to test location class'''
    def setUp(self):
        '''Function to prepare for every test case'''
        self.test_location = Location(location = 'Eldoret')

    def tearDown(self):
        '''Function to clean up after every test case'''
        Location.objects.all().delete()

    def test_isinstance(self):
        '''Test if test_location is an instance of location class'''
        self.assertTrue(isinstance(self.test_location, Location))
    def test_save_location(self):
        '''Test saving a location to database'''
        self.test_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        '''Test deleting a location'''
        self.test_location.save_class()
        self.test_location.delete_class()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_update_location(self):
        '''Test case to update a location in database'''
        self.test_location.save_class()
        self.test_location.update_class(location = 'Kisumu')
        self.assertEqual(self.test_location.location, 'Kisumu')

class TestCategories(TestCase):
    '''Test class to test categories class'''
    def setUp(self):
        '''Function to prepare for every test case'''
        self.test_categories = Categories(categories= 'landscape')

    def tearDown(self):
        '''Function to clean up after every test case'''
        Categories.objects.all().delete()

    def test_isinstance(self):
        '''Test if test_category is an instance of category class'''
        self.assertTrue(isinstance(self.test_categories, Categories))

    def test_save_categories(self):
        '''Test saving a category to database'''
        self.test_categories.save_class()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_categories(self):
        '''Test deleting a category'''
        self.test_categories.save_class()
        self.test_categories.delete_class()
        categories = Categories.objects.all()
        self.assertTrue(len(categories) == 0)

    def test_update_categories(self):
        '''Test case to update a category in database'''
        self.test_categories.save_class()
        self.test_categories.update_class(categories = 'adventure')
        self.assertEqual(self.test_categories.categories, 'adventure')
