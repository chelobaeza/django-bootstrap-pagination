pagination
===========================



Quick start
-----------

1. Download django-bootstrap-pagination app.
Passing a branch name, a commit hash, a tag name or a git ref is possible like so::

    pip install [opt]

    opt:
        git+https://github.com/chelobaeza/django-bootstrap-pagination.git@master#egg=django-bootstrap-pagination
        git+https://github.com/chelobaeza/django-bootstrap-pagination.git@v1.0#egg=django-bootstrap-pagination
	git+https://github.com/chelobaeza/django-bootstrap-pagination.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=django-bootstrap-pagination
	git+https://github.com/chelobaeza/django-bootstrap-pagination.git@refs/pull/123/head#egg=django-bootstrap-pagination


2. Add "pagination" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'pagination',
    ]


3. Load the pagination templatetag::

	{% load pagination %}

4. Call the tag to render the pagination html::

	{% paginate %}

