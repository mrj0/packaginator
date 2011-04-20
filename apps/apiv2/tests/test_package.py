from django.core.urlresolvers import reverse
from apps.apiv2.tests.data import Apiv2TestCase
import json


class PackageV2Tests(Apiv2TestCase):
    def test_01_root_packages(self):
        urlkwargs_pkg1 = {
            'slug': self.pkg1.slug,
        }
        url_pkg1 = reverse('api2-package-root-resource')
        response_pkg1 = self.client.get(url_pkg1)
        # check that the request was successful
        self.assertEqual(response_pkg1.status_code, 200)
        # check that we have a usage_count equal to the one in the DB
        raw_json = response_pkg1.content
        packages = json.loads(raw_json)
        self.assertEqual(len(packages), 2)
        
    def test_02_root_packages_search(self):
        urlkwargs_pkg1 = {
            'slug': self.pkg1.slug,
        }
        url_pkg1 = reverse('api2-package-root-resource')
        response_pkg1 = self.client.get(url_pkg1, {'slug': 'package2'})
        # check that the request was successful
        self.assertEqual(response_pkg1.status_code, 200)
        # check that we have a usage_count equal to the one in the DB
        raw_json = response_pkg1.content
        packages = json.loads(raw_json)
        self.assertEqual(len(packages), 1)
        
    def test_03_packages_usage(self):
        urlkwargs_pkg1 = {
            'slug': self.pkg1.slug,
        }
        url_pkg1 = reverse('api2-package-resource', kwargs=urlkwargs_pkg1)
        response_pkg1 = self.client.get(url_pkg1)
        # check that the request was successful
        self.assertEqual(response_pkg1.status_code, 200)
        # check that we have a usage_count equal to the one in the DB
        raw_json_pkg1 = response_pkg1.content
        pkg_1 = json.loads(raw_json_pkg1)
        usage_count_pkg1 = int(pkg_1['usage_count'])
        self.assertEqual(usage_count_pkg1, self.pkg1.usage.count())
        # do the same with pkg2
        urlkwargs_pkg2 = {
            'slug': self.pkg2.slug,
        }
        url_pkg2 = reverse('api2-package-resource', kwargs=urlkwargs_pkg2)
        response_pkg2 = self.client.get(url_pkg2)
        # check that the request was successful
        self.assertEqual(response_pkg2.status_code, 200)
        # check that we have a usage_count equal to the one in the DB
        raw_json_pkg2 = response_pkg2.content
        pkg_2 = json.loads(raw_json_pkg2)
        usage_count_pkg2 = int(pkg_2['usage_count'])
        self.assertEqual(usage_count_pkg2, self.pkg2.usage.count())

