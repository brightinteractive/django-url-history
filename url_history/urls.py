# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

from django.conf.urls import patterns, url

urlpatterns = patterns('url_history.views',
    # Only for use by tests - doesn't add any useful functionality in production
    # (server_error is supposed to be used by assigning it to handler500)
    url(r'^test-server-error$', 'server_error', name='test-server-error'),
)
