#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies
a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier
  Args:
      multiplier (float):
  Returns:
      Callable[[float], float]:
    """
    def multi(value: float) -> float:
        """ return mutli * multi"""
        return value * multiplier
    return multi
