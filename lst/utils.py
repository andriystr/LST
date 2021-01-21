# -*- coding: utf-8 -*-


def flatten(seq):
    if hasattr(seq, '__iter__') and not isinstance(seq, (str, bytes, bytearray)):
        for val in seq:
            yield from flatten(val)
    else:
        yield seq
