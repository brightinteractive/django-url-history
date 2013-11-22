# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

from url_history.models import  _get_url_history_queue, _set_url_history_queue


class URLHistoryMiddleware(object):
    """
    Stores the most recently visited URLs in the session.

    Requires sessions to be enabled.
    """

    def process_request(self, request):
        history = _get_url_history_queue(request.session)
        history.append(request.get_full_path())

        _set_url_history_queue(request, history)
