from django.core.urlresolvers import reverse
from django.db.models.fields import FieldDoesNotExist
from django.db.models.sql.constants import LOOKUP_SEP, QUERY_TERMS

from djangorestframework.modelresource import Resource, ModelResource, RootModelResource, QueryModelResource
from apps.package.models import Package, Category
from apps.grid.models import Grid, GridPackage
from apps.homepage.models import Dpotw, Gotw

# must list the fields or the framework will only serialize the
# model fields, not any augmented fields
PACKAGE_FIELDS = (
    "category",
    "commits_over_52",
    "created",
    "grids",
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

class FilterNotAllowed(Exception):
    pass

# following the example of core django 
# http://code.djangoproject.com/changeset/15033
def lookup_allowed(model, lookup, value):
    # Check FKey lookups that are allowed, so that popups produced by
    # ForeignKeyRawIdWidget, on the basis of ForeignKey.limit_choices_to,
    # are allowed to work.
    for l in model._meta.related_fkey_lookups:
        for k, v in widgets.url_params_from_lookup_dict(l).items():
            if k == lookup and v == value:
                return True

    parts = lookup.split(LOOKUP_SEP)

    # Last term in lookup is a query term (__exact, __startswith etc)
    # This term can be ignored.
    if len(parts) > 1 and parts[-1] in QUERY_TERMS:
        parts.pop()

    # Special case -- foo__id__exact and foo__id queries are implied
    # if foo has been specificially included in the lookup list; so
    # drop __id if it is the last part. However, first we need to find
    # the pk attribute name.
    pk_attr_name = None
    for part in parts[:-1]:
        field, _, _, _ = model._meta.get_field_by_name(part)
        if hasattr(field, 'rel'):
            model = field.rel.to
            pk_attr_name = model._meta.pk.name
        elif isinstance(field, RelatedObject):
            model = field.model
            pk_attr_name = model._meta.pk.name
        else:
            pk_attr_name = None
    if pk_attr_name and len(parts) > 1 and parts[-1] == pk_attr_name:
        parts.pop()

    try:
        model._meta.get_field_by_name(parts[0])
    except FieldDoesNotExist:
        return False
    else:
        return True

class PackageRootResource(QueryModelResource):
    """A query resource for Package. (Limited to 20 results.)"""
    model = Package
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = PACKAGE_FIELDS

    def get(self, request, auth, *args, **kwargs):
        query = self.model.objects.all().filter(**kwargs)

        # rest framework's internal override parameters start with '_'
        for key in [key for key in request.GET.keys() if not key.startswith('_')]:
            value = request.GET[key]
            if lookup_allowed(self.model, key, value):
                query = query.filter(**{key: value})
            else:
                raise FilterNotAllowed, 'Invalid filter name'
        packages = query[:20]
        for package in packages:
            package.usage_count = package.get_usage_count() or '0'
            package.grids = [reverse('api2-grid-resource', args=[grid.slug]) for grid in package.grids()]
        return packages

class PackageResource(ModelResource):
    model = Package
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = PACKAGE_FIELDS

    def get(self, request, auth, *args, **kwargs):
        package = ModelResource.get(self, request, auth, *args, **kwargs)
        if package:
            package.usage_count = package.get_usage_count() or '0' # bug in framework, doesn't include 0 values for these fields
            package.grids = [reverse('api2-grid-resource', args=[grid.slug]) for grid in package.grids()]
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

GRID_FIELDS = (
    'created',
    'description',
    'modified',
    'slug',
    'title',
    )

class GridRootResource(RootModelResource):
    """a list of all grids"""
    model = Grid
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = GRID_FIELDS

class GridResource(ModelResource):
    model = Grid
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = GRID_FIELDS

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

