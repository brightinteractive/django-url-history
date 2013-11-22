# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

from django import http
from django.template import loader
from django.template.context import Context
from django.utils.log import getLogger
from django.views.decorators.csrf import requires_csrf_token
import uuid
from url_history.models import url_history

logger = getLogger('django.request')


@requires_csrf_token
def server_error(request, template_name='500.html', data=None):
    """
    500 error handler that logs the URL history and an error ID, and shows the
    error ID to the user so that a developer can find it in the logs later.

    Templates: `500.html`
    Context:
        error_id
            A unique identifier for the error that just happened.
    """

    error_id = str(uuid.uuid4())
    logger.error('Error ID: %s. URLs leading up to this error: %s',
        error_id, url_history(request.session))

    t = loader.get_template(template_name)

    if data:
        data = dict(data)
    else:
        data = dict()
    data['error_id'] = error_id
    result = http.HttpResponseServerError(t.render(Context(data)))
    return result
