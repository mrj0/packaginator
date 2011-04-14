from djangorestframework.modelresource import Resource, ModelResource, RootModelResource
from apps.package.models import Package

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

class PackageRootResource(RootModelResource):
    """a list resource for Package."""
    model = Package
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = PACKAGE_FIELDS

class PackageResource(ModelResource):
    model = Package
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    fields = PACKAGE_FIELDS

    def get(self, request, auth, *args, **kwargs):
        package = ModelResource.get(self, request, auth, *args, **kwargs)
        if package:
            package.usage_count = package.get_usage_count() or '0' # bug in framework, doesn't include 0 values
            package.grids = [grid.get_absolute_url() for grid in package.grids()]
        return package

