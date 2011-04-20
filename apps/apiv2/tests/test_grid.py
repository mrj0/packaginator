from django.core.urlresolvers import reverse
from apps.apiv2.tests.data import Apiv2TestCase
import json


class GridV2Tests(Apiv2TestCase):
    def test_root_grid(self):
        url = reverse('api2-grid-root-resource')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        rawjson = response.content
        self.assertEqual(len(json.loads(rawjson)), 1)

    def test_grid_slug(self):
        url = reverse('api2-grid-resource', kwargs={'slug': self.grid.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        rawjson = response.content
        self.assertEqual(json.loads(rawjson)['slug'], self.grid.slug)

    def test_grid_packages(self):
        url = reverse('api2-grid-packages-resource', kwargs={'slug': self.grid.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        rawjson = response.content
        self.assertEqual(len(json.loads(rawjson)), 2)
        
