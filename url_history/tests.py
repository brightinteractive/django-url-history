# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

"""
Tests for the history functionality that is used to provide a URL history with
bug reports.
"""

from django.core.urlresolvers import reverse
from url_history.models import url_history
import django.test


class TestCase(django.test.TestCase):
    tags = ['service', ]


class HistoryTests(TestCase):

    def test_basic_history(self):
        urls = [
            '/first',
            '/something/second',
            '/something/third/'
            ]

        # visit the urls
        for url in urls:
            self.client.get(url)

        self.assertEqual(
            urls,
            url_history(self.client.session))

        # visit another url and check that the history changed
        new_url = '/four444th'
        self.client.get(new_url)
        urls.append(new_url)

        self.assertEqual(
            urls,
            url_history(self.client.session))

    def test_query_params_saved(self):
        url_with_params = '/assets/42/resize?width=200&height=300'
        self.assertContainsQueryString(url_with_params)

        self.client.get(url_with_params)

        self.assertEqual(
            [url_with_params],
            url_history(self.client.session)
        )

    def assertContainsQueryString(self, url):
        self.assertIn('?', url)

    def test_history_is_bounded(self):
        request_count = 50
        url = '/first'
        for i in xrange(request_count):
            self.client.get(url)
        self.assertLess(len(url_history(self.client.session)),
                        request_count)


class HistoryServerErrorViewTests(TestCase):
    """
    Tests for url_history.views.server_error.

    Depend on django-raise-exception-view being installed and it's urls.py
    being included in the urlconf.
    """

    def test_error_id_included_in_error_context(self):
        urls = [
            '/first11?foo=bar',
            '/something/second',
            '/tird/'
            ]

        # visit the urls
        for url in urls:
            self.client.get(url)

        response = self.client.get(reverse('test-server-error'))

        self.assertEqual(500, response.status_code)
        self.assertIsNotNone(response.context['error_id'])

    def test_error_ids_unique(self):
        error_id1 = self._call_server_error_view_and_return_error_id()
        error_id2 = self._call_server_error_view_and_return_error_id()
        self.assertNotEqual(error_id1, error_id2)

    def _call_server_error_view_and_return_error_id(self):
        response = self.client.get(reverse('test-server-error'))
        self.assertEqual(500, response.status_code)
        error_id = response.context['error_id']
        return error_id
