from django.conf.urls.defaults import patterns, url
from apps.apiv2.views import (PackageResource,
                              CategoryRootResource, CategoryResource,
                              GridRootResource, GridResource,
                              GridPackageRootResource,
                              DpotwResource,
                              GotwResource)

urlpatterns = patterns(
    'modelresourceexample.views',
    url(r'^package/(?P<slug>[-\w]+)/$', PackageResource.as_view(), name='api2-package-resource'),

    url(r'^category/$', CategoryRootResource.as_view(), name='api2-category-root-resource'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryResource.as_view(), name='api2-category-resource'),

    url(r'^grid/$', GridRootResource.as_view(), name='api2-grid-root-resource'),
    url(r'^grid/(?P<slug>[-\w]+)/$', GridResource.as_view(), name='api2-grid-resource'),

    url(r'^grid/(?P<slug>[-\w]+)/packages/$', GridPackageRootResource.as_view(), name='api2-grid-resource'),

    url(r'^package-of-the-week/$', DpotwResource.as_view(), name='api2-dpotw-resource'),

    url(r'^grid-of-the-week/$', GotwResource.as_view(), name='api2-gotw-resource'),
)
