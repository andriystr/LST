# -*- coding: utf-8 -*-

__all__ = []


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

