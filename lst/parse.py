# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs


class Parsed:
    def __init__(self, content=b'', url='', **kwargs):
        self.content = content
        self.url = url
        self._args = kwargs

    def __getitem__(self, name):
        return self._args[name]

    def __setitem__(self, name, value):
        self._args[name] = value

    def __contains__(self, name):
        return name in self._args

    def __delitem__(self, name):
        del self._args[name]

