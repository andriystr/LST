# -*- coding: utf-8 -*-

import logging
from concurrent.futures import ThreadPoolExecutor


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
fmt = logging.Formatter('%(name)s:line %(lineno)s:%(asctime)s:\n%(message)s')
handler.setFormatter(fmt)
logger.addHandler(handler)
logger.setLevel(logging.WARNING)

