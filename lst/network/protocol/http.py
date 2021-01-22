# -*- coding: utf-8 -*-

from ..protocol import Request
from ..response import create_response


import requests


class ContentStream:
    def __init__(self, resp_iter):
        self._resp_iter = resp_iter
        #TODO


def _get_type(resp):
    pass
    #TODO


def fetch(url, method='GET', **kwargs):
    s_req_kwargs = (
        'params', 'data', 'json', 'headers',
        'cookies', 'files', 'auth', 'timeout',
        'allow_redirects', 'proxies', 'verify',
        'stream', 'cert'
    )
    args = {
        key: val
        for key, val in kwargs.items()
        if key in s_req_kwargs
    }
    resp = requests.request(method, url, **args)

    s_req_attrs = (
        'method', 'headers', 'files',
        'data', 'json', 'params',
        'auth', 'cookies', 'hooks'
    )
    req_args = {
        key: val
        for key, val in vars(resp.request).items()
        if key in s_req_attrs
    }
    req = Request(url, **req_args)

    s_resp_attrs = (
        'status_code', 'headers', 'url', 'history',
        'encoding', 'reason', 'cookies', 'elapsed'
    )
    resp_args = {
        key: val
        for key, val in vars(resp).items()
        if key in s_resp_attrs
    }
    stream = ContentStream(resp.iter_content())
    return create_response(url, stream, _get_type(resp), req, **resp_args)

