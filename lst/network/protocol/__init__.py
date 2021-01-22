# -*- coding: utf-8 -*-

__all__ = ['fetch', 'Request']


from urllib.parse import urlparse


import http
import file
import data


class URLError(OSError):
    pass


def fetch(url, **kwargs):
    parse_res = urlparse(url)
    scheme = parse_res.scheme
    if scheme == 'http' or scheme == 'https':
        return http.fetch(url, **kwargs)
    elif scheme == 'file':
        return file.fetch(url, **kwargs)
    elif scheme == 'data':
        return data.fetch(url, **kwargs)
    else:
        raise URLError(
            'unknown url type: %s' % scheme
        )


class Request:
    def __init__(self, url, **kwargs):
        self.url = url
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
