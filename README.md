django-bylaws
================

This project gives you a pluggable application for adding bylaws to a
project. It takes advantage of django_simple_history to provide
rudimentary version control of your bylaw documents and can also handle
whether users must sign them before doing various deeds on your website.

Installation
-------------

1. Place 'bylaws' in your installed apps.
2. Add something like the following to your urls:

        url(r'^bylaws/', include('bylaws.urls')),

3. Sync your DB:

        python manage.py syncdb

Overview
----------

Bylaws are simple documents that allow you to:

1. use markup to structure a bylaws document
2. keep track of any changes anyone makes
3. gives you easy access to the latest adopted bylaw document
