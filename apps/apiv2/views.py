from django.core.urlresolvers import reverse

from djangorestframework.modelresource import Resource, ModelResource, RootModelResource
from apps.package.models import Package, Category
from apps.grid.models import Grid, GridPackage
from apps.homepage.models import Dpotw, Gotw

# must list the fields or the framework will only serialize the
# model fields, not any augmented fields
PACKAGE_FIELDS = (
    "absolute_url",
    "category",
    "commits_over_52",
    "created",
    "created_by",
    "grids",
    "id",
    "last_modified_by",
    "modified",
    "participants",
    "pypi_downloads",
    "pypi_home_page",
    "pypi_url",
    "pypi_version",
    "repo_commits",
    "repo_description",
    "repo_forks",
    "repo_url",
    "repo_watchers",
    "resource_uri",
    "slug",
    "title",
    "usage_count",
    )

class PackageResource(ModelResource):
    model = Package
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = PACKAGE_FIELDS

    def get(self, request, auth, *args, **kwargs):
        package = ModelResource.get(self, request, auth, *args, **kwargs)
        if package:
            package.usage_count = package.get_usage_count() or '0' # bug in framework, doesn't include 0 values for these fields
            package.grids = [grid.get_absolute_url() for grid in package.grids()]
        return package

class CategoryRootResource(RootModelResource):
    """a list resource for Category."""
    model = Category
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)

class CategoryResource(ModelResource):
    model = Category
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)

class GridRootResource(RootModelResource):
    """a list of all grids"""
    model = Grid
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)

class GridResource(ModelResource):
    model = Grid
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)

class GridPackageRootResource(RootModelResource):
    """a list of all packages related to a grid"""
    model = Package
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = PACKAGE_FIELDS

    def get(self, request, auth, *args, **kwargs):
        grid = Grid.objects.get(slug=kwargs['slug'])
        if grid:
            return [ grid_package.package for grid_package in GridPackage.objects.filter(grid=grid)]
        return None

class DpotwResource(ModelResource):
    """The package of the week"""
    model = Dpotw
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = ('start_date', 'end_date', 'modified', 'resource_uri', 'created',)

    def get(self, request, auth, *args, **kwargs):
        query = Dpotw.objects.get_current()
        if len(query) < 1:
            return query
        dpotw = query[0]
        dpotw.resource_uri = reverse('api2-package-resource', args=[dpotw.package.slug])
        return dpotw

class GotwResource(ModelResource):
    """The package of the week"""
    model = Gotw
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = ('start_date', 'end_date', 'modified', 'resource_uri', 'created',)

    def get(self, request, auth, *args, **kwargs):
        query = Gotw.objects.get_current()
        if len(query) < 1:
            return query
        gotw = query[0]
        gotw.resource_uri = reverse('api2-grid-resource', args=[gotw.grid.slug])
        return gotw

