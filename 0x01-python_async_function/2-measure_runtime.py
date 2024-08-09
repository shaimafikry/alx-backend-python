#!/usr/bin/env python3
"""
  calculate the time of the async
  """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


# From the previous file, import wait_n into 2-measure_runtime.py.
# Create a measure_time function with integers n and max_delay
# as arguments that measures the total execution time for
# wait_n(n, max_delay), and returns total_time / n.
# Your function should return a float.
# Use the time module to measure an approximate elapsed time.
def measure_time(n: int, max_delay: int) -> float:
    """clculate the time of async func
    Args:
        n (int): range of loop
        max_delay (int): range of delay

    Returns:
        float: time spent
    """
    tme1 = time.time()
    asyncio.run(wait_n(n, max_delay))  # Run wait_n in an event loop
    tme2 = time.time()
    return (tme2 - tme1) / n
