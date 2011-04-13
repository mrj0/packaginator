from djangorestframework.modelresource import ModelResource, RootModelResource
from apps.package.models import Package

class PackageRootResource(RootModelResource):
    """a list resource for Package."""
    model = Package
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)

class PackageResource(ModelResource):
    model = Package
    authenticators = ()
    allowed_methods = anon_allowed_methods = ('GET',)
    
