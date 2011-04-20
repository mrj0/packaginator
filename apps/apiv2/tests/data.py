from django.contrib.auth.models import User
from django.test import TestCase

from grid.models import Grid, GridPackage
from package.models import Package, Category

class Apiv2TestCase(TestCase):
    def setUp(self):
        """
        Set up initial data for this package of tests
        """
        self.category = Category.objects.create(
            title='App',
            slug='app',
        )
        self.grid = Grid.objects.create(
            title='A Grid',
            slug='grid',
        )
        self.pkg1 = Package.objects.create(
            title='Package1',
            slug='package1',
            category=self.category,
            repo_url='https://github.com/pydanny/django-uni-form'
        )
        self.pkg2 = Package.objects.create(
            title='Package2',
            slug='package2',
            category=self.category,
            repo_url='https://github.com/cartwheelweb/packaginator'  
        )
        GridPackage.objects.create(package=self.pkg1, grid=self.grid)
        GridPackage.objects.create(package=self.pkg2, grid=self.grid)
        self.user = User.objects.create_user('user', 'user@packaginator.com', 'user')
        self.pkg1.usage.add(self.user)
