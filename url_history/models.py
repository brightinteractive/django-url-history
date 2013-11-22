# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

import collections


URL_HISTORY_KEY = 'url_history'
MAX_HISTORY_LENGTH = 20


def _get_url_history_queue(session):
    return collections.deque(
        iterable=_get_url_history_list(session),
        maxlen=MAX_HISTORY_LENGTH)


def _get_url_history_list(session):
    return session.get(URL_HISTORY_KEY,
                       [])


def _set_url_history_queue(request, history):
    request.session[URL_HISTORY_KEY] = list(history)


def url_history(session):
    """
    Return the last few URLs that were accessed in the given Django session.

    Only works if URLHistoryMiddleware is enabled.
    """

    return _get_url_history_list(session)
