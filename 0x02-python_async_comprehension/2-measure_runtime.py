#!/usr/bin/env python3
"""write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.
  """
import asyncio
import time
async_comperhension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure run time
    Returns:
        float: total time
    """
    strt = time.time()
    test = await asyncio.gather(async_comperhension(),
                                async_comperhension(),
                                async_comperhension(),
                                async_comperhension())
    end = time.time()
    return end - strt
