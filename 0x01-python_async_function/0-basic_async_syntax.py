#!/usr/bin/env python3
"""
task on async func
"""
# Write an asynchronous coroutine that takes in an integer argument
# (max_delay, with a default value of 10) named wait_random that waits
# for a random delay between 0 and max_delay (included and float value)
# seconds and eventually returns it.
# Use the random module.
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """takes an int and wait btw
      0, max_delay
    Args:
        max_delay (int): _description_
    """
    time_delay = random.uniform(0, max_delay)
    await asyncio.sleep(time_delay)
    return time_delay
