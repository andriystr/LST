# -*- coding: utf-8 -*-

__all__ = []


from urllib.parse import urljoin


from ..protocol import fetch
from ..protocol import Request


class Response:
    def __init__(self, url='', request=Request(''), **kwargs):
        self.url = url
        self.request = request
        self._args = kwargs

    def __getattr__(self, name):
        if name in self._args:
            return self._args[name]
        else:
            raise AttributeError(
                '\'%s\' object has no attribute \'%s\'' % (
                    type(self).__name__,
                    name
                )
            )

    def __setattr__(self, name, value):
        if name in self._args:
            return self._args[name] = value
        else:
            raise AttributeError(
                '\'%s\' object has no attribute \'%s\'' % (
                    type(self).__name__,
                    name
                )
            )

    def has(self, name):
        return name in self._args

    def urljoin(self, url):
        return urljoin(self.url, url)

    def follow(self, url, **kwargs):
        return fetch(self.urljoin(url), **kwargs)

