from django.conf.urls.defaults import patterns, url
from apps.apiv2.views import PackageRootResource, PackageResource

urlpatterns = patterns('modelresourceexample.views',
    url(r'^package/$', PackageRootResource.as_view(), name='package-root-resource'),
    url(r'^package/(?P<slug>[-\w]+)/$', PackageResource.as_view(), name='package-resource'),
    url(r'^packages/p/(?P<slug>[-\w]+)/$', PackageResource.as_view(), name='packages-resource'),
)
