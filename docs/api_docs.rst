==============
Webservice API
==============

This is the API documentation for Packaginator. It is designed to be language and tool agnostic.

API Usage
=========

The current API is limited to read-only GET requests. Other HTTP methods will fail.

API Reference
=============

Representation Formats
-----------------------

Representation formats

* application/json
* text/html
* application/xhtml+xml
* text/plain
* application/xml
* UTF-8.

Base URI
--------

============================ ======== =======
URI                          Resource Methods           
============================ ======== =======
<http-my-domain.com>/api/v2/ Root     GET
============================ ======== =======

URIs
----

==============================================  ======================= ==================
URI                                             Resource                Methods           
==============================================  ======================= ==================
/`category`_/                                   Category list           GET
/`category`_/{slug}/                            Category                GET
/`grid`_/                                       Grid list               GET
/`grid`_/{slug}/                                Grid                    GET
/`grid`_/{slug}`/packages`_/                    Grid Packages list      GET
/`grid-of-the-week`_/                           Featured Grid           GET
/`package`_/                                    Package list            GET
/`package`_/{slug}/                             Package                 GET
/`package-of-the-week`_/                        Featured Package        GET
==============================================  ======================= ==================

Resources
---------

Category
~~~~~~~~

Representation:

.. parsed-literal::


    {
        "created": "2010-08-14 19:47:52", 
        "description": "Small components used to build projects. An app is anything that is installed by placing in settings.INSTALLED_APPS.", 
        "modified": "2010-09-12 19:42:58", 
        "show_pypi": true, 
        "slug": "apps", 
        "title": "App", 
        "title_plural": "Apps"
    }
    
Grid
~~~~

Representation:

.. parsed-literal::

    {
        "created": "2010-08-14 20:12:46", 
        "description": "This page lists a few well-known reusable Content Management System applications for Django and tries to gather a comparison of essential features in those applications.", 
        "modified": "2011-04-10 16:44:28.380734", 
        "slug": "cms", 
        "title": "CMS"
    }

Grid-of-the-week
~~~~~~~~~~~~~~~~

Representation:

.. parsed-literal::

    {
        "created": "2011-01-08 15:58:56", 
        "end_date": "2011-12-31", 
        "modified": "2011-01-08 15:58:56", 
        "resource_uri": "http://djangopackages.com/api/v2/grid/flash/", 
        "start_date": "2011-01-07"
    }
    
Package
~~~~~~~

Representation:

.. parsed-literal::

    {
        "category": {
            "created": "2010-08-14 19:48:52", 
            "description": "Large efforts that combine many python modules or apps. Examples include Django, Pinax, and Satchmo. Most CMS falls into this category.", 
            "modified": "2010-09-12 19:43:04", 
            "show_pypi": true, 
            "slug": "frameworks", 
            "title": "Framework", 
            "title_plural": "Frameworks"
        }, 
        "commits_over_52": "0,0,0,0,0,0,0,0,0,0,0,0,0,23,12,0,0,0,0,0,19,0,1,0,0,1,4,0,0,1,3,0,0,0,1,5,6,1,1,5,0,1,0,0,1,0,3,0,0,8,0,0", 
        "created": "2010-08-16 23:25:16", 
        "grids": [
            "http://djangopackages.com/api/v2/grid/this-site/", 
            "http://djangopackages.com/api/v2/grid/profiles/", 
            "http://djangopackages.com/api/v2/grid/social/"
        ], 
        "modified": "2011-04-10 01:06:20.662306", 
        "participants": "pydanny", 
        "pypi_downloads": 0, 
        "pypi_home_page": null, 
        "pypi_url": "http://pypi.python.org/pypi/Pinax", 
        "pypi_version": "0.9a1", 
        "repo_commits": 0, 
        "repo_description": "a Django-based platform for rapidly developing websites", 
        "repo_forks": 206, 
        "repo_url": "https://github.com/pinax/pinax", 
        "repo_watchers": 1179, 
        "slug": "pinax", 
        "title": "Pinax", 
        "usage_count": 27
    }
    
Package-of-the-week
~~~~~~~~~~~~~~~~~~~

Representation:

.. parsed-literal::

    {
        "created": "2011-01-08 15:57:55", 
        "end_date": "2011-12-31", 
        "modified": "2011-01-08 15:57:55", 
        "resource_uri": "http://djangopackages.com/api/v2/package/django-cumulus/", 
        "start_date": "2011-01-07"
    }
