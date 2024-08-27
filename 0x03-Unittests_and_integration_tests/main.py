#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
from unittest.mock import Mock, patch

import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


def get_json(url: str) -> Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()




with patch.object(Mock, get_json, retunr_value="none ter"):
    print(get_json('wwwd'))
