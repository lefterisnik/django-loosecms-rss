======================
Django Loose CMS - Rss
======================

A rss plugin for Django Loose CMS.

Requirements
------------

Loose CMS Text plugin requires:

* Django version 1.8
* Python 2.6 or 2.7
* django-loose-cms
* feedparser,
* python-memcached

Quick Start
-----------

1. Instalation via pip::

    pip install https://github.com/lefterisnik/django-loosecms-rss/archive/master.zip

2. Add "loosecms_rss" to your INSTALLED_APPS setting after "loosecms" like this::

    INSTALLED_APPS = (
        ...
        'loosecms_rss',
    )
    
3. Run ``python manage.py migrate`` to create the loosecms_rss models.

4. Run development server ``python manage.py runserver`` and visit http://127.0.0.1:8000/ to start
   playing with the cms.

5. You will need to install the ``memcached`` mechanism in your system. Python-memcached is only the python binding to
   speak with memcached. To install the memcached package in ubuntu::

    sudo apt-get install memcached