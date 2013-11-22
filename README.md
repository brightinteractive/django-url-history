Django URL History
==================

**Store the last few URLs visited in the session and then log them in the `server_error` view, to aid debugging.**

**Author:** [Bright Interactive][1].


Adding it to your Django Project
================================

Install:

    pip install django-url-history

Add to your MIDDLEWARE_CLASSES setting:

    MIDDLEWARE_CLASSES = (
        ...
        'url_history.middleware.URLHistoryMiddleware',
        ...
    )

You can then add a server_error view to your app's `views.py` which will log the last few URLs that a user visited before they encountered an error:

    import url_history.views
    
    def server_error(request, *args, **kwargs):
        return url_history.views.server_error(
            request, data={
                'PROJECT_NAME': settings.PROJECT_NAME,
                'SUPPORT_EMAIL_ADDRESS': settings.SUPPORT_EMAIL_ADDRESS,
            },
            *args, **kwargs)

...and then enable this by adding the following to your project's main `urls.py`:

    handler500 = 'yourapp.views.server_error'
    
...and showing the error ID in your project's `500.html` template:

    <p>
        If the problem persists, <a id="id_contact_us" href="mailto:{{ SUPPORT_EMAIL_ADDRESS }}{% if error_id %}?subject={{ PROJECT_NAME|urlencode }}%20Error:%20{{ error_id }}{% endif %}">contact us</a>{% if error_id %}, quoting error ID {{ error_id }},{% endif %}
        and we'll help you get on your way.
    </p>


Publishing releases to PyPI
===========================

To publish a new version of django-url-history to PyPI, set the `__version__` 
string in `url_history/__init__.py`, then run:

    # Run the tests against multiple environments
    tox
	# Publish to PyPI
    ./setup.py publish
	# Tag (change 1.0.0 to the version you are publishing!)
	git tag -a v1.0.0 -m 'Version 1.0.0'
	git push --tags


Running the tests
=================

To run the tests against the current environment:

    ./manage.py test

To run the tests against multiple environments, install `tox` using
`pip install tox`, make sure you're not currently in a virtual environment,
then simply run `tox`:

    tox


Changelog
=========

1.0.0
-----

* Initial release


License
=======

Copyright (c) Bright Interactive Limited.
Started with django-reusable-app Copyright (c) DabApps.

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[1]: http://www.bright-interactive.com/
