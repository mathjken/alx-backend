#!/usr/bin/env python3
'''
    Simple helper function.
'''


def index_range(page, page_size):
    '''
        Returns a tuple of size two corresponding to the range of indices
        for a given page.
    '''
    begin = (page - 1) * page_size
    stop = page * page_size
    return begin, stop
