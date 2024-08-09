#!/usr/bin/env python3
"""
    application on async and delay
    """
# Import wait_random from the previous python file that you’ve
# written and write an async routine called wait_n that takes
# in 2 int arguments (in this order): n and max_delay.
# You will spawn wait_random n times with the specified max_delay.
# wait_n should return the list of all the delays (float values).
# The list of the delays should be in ascending order without
# using sort () because of concurrency.
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spwan wait_random n times
    Args:
        n (int): times of spwan
        max_delay (int): range of delay

    Returns:
        List[float]: _description_
    """
    list_of_random = [wait_random(max_delay) for i in range(n)]
    # to get all the results at one list at once
    results = await asyncio.gather(*list_of_random)
    results.sort()
    # for i in range(n):
    #     delay: float = await wait_random(max_delay)
    #     list_of_random.append(delay)
    # temp = list_of_random[0]
    # for i in range(n):
    #     if temp < list_of_random[i]:
    #         hold = list_of_random[i]
    #         list_of_random[i] = temp
    #         temp = hold
    return results
