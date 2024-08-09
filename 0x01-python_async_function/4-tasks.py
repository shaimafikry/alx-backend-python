#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into
a new function task_wait_n. The code is nearly identical to
wait_n except task_wait_random is being called
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spwan wait_random n times
    Args:
        n (int): times of spwan
        max_delay (int): range of delay

    Returns:
        List[float]: _description_
    """
    list_of_random = [asyncio.create_task(wait_random(max_delay))
                      for _ in range(n)]
    # to get all the results at one list at once
    results: List[float] = []
    for task in asyncio.as_completed(list_of_random):
        delay = await task
        results.append(delay)
    return results
