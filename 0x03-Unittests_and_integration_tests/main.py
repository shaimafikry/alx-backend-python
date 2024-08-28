#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
# import random
# from unittest.mock import Mock, patch
 
 
# days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri' , 'sat']
 
# # random.choice = Mock(return_value='wed')
# print(random.choice(days))

# #using patch
# with patch('random.choice', return_value='wed'):
#     print(random.choice(days))


def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)


class more:
  
    @memoize()
    def test(self):
        print ('wow')

m = more()
m.test
