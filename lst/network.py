# -*- coding: utf-8 -*-

from urllib.parse import urlparse

from parse import Parsed

import requests


class URLSchemeError(ValueError):
    pass


def fetch(url, **kwargs):
    url_parsed = urlparse(url)
    scheme = url_parsed.scheme
    if scheme.startswith('http'):
        method = kwargs.get('method', 'GET')
        resp = requests.request(method, url, **kwargs)
        return Parsed(resp.content, resp.url, response=resp)
    else:
        raise URLSchemeError('unknown url scheme \'%s\'' % scheme)
