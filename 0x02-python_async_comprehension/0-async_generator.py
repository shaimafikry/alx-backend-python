#!/usr/bin/env python3
"""
    Write a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10.
    Use the random module.
    Yields:
  """
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, float]:
    """loop through async
    Yields:
        int: random value
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
