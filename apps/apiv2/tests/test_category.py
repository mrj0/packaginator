from django.core.urlresolvers import reverse
from apps.apiv2.tests.data import Apiv2TestCase
import json


class CategoryV2Tests(Apiv2TestCase):
    def test_01_catagories_usage(self):
        urlkwargs_pkg1 = {
            'slug': self.category.slug,
        }
        url_pkg1 = reverse('api2-category-resource', kwargs=urlkwargs_pkg1)
        response_pkg1 = self.client.get(url_pkg1)
        # check that the request was successful
        self.assertEqual(response_pkg1.status_code, 200)
