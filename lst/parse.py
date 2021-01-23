# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs


class Parsed:
    def __init__(self, content=b'', url='', **kwargs):
        self.content = content
        self.url = url
        self._args = kwargs

