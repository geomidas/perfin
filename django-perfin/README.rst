=====
perfin
=====

perfin is a Django app to conduct Web-based perfin. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "perfin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'perfin',
    ]

2. Include the perfin URLconf in your project urls.py like this::

    path('perfin/', include('perfin.urls')),

3. Run ``python manage.py migrate`` to create the perfin models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/perfin/ to participate in the poll.