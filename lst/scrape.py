# -*- coding: utf-8 -*-

import logging
import traceback


import requests

from monapy import Binder
from monapy import Step
from bs4 import Tag
from bs4 import BeautifulSoup as bs


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
fmt = logging.Formatter('%(name)s:line %(lineno)s:%(asctime)s:\n%(message)s')
handler.setFormatter(fmt)
logger.addHandler(handler)
logger.setLevel(logging.WARNING)

