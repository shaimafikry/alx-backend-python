#!/usr/bin/env python3
"""Given the parameters and the return values, add type annotations to the function
"""
from typing import Union, Any, Mapping, T

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """intdo to typing of maping and any
    """
    if key in dct:
        return dct[key]
    else:
        return default
