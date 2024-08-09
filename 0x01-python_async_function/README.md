# Async
After importing asyncio
	```
	import asyncio
	```

1. Async and Await Syntax
async: Used to define an asynchronous function, which returns a coroutine object.
await: Pauses the execution of the coroutine on which it is used, waiting for the result of an awaited coroutine or future.

2- asyncio.sleep(n) => wait for n time in miliesecond
3- asyncio.run(fun) => to run async func
4- asyncio.gather(one, two) => to gather more than one func to be excuted

```
import asyncio

async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)  # Simulate an I/O-bound operation with sleep
    print("Done fetching data!")
    return "Data"

async def main():
    result = await fetch_data()  # Await the coroutine
    print(result)

# Running the async function using asyncio.run()
asyncio.run(main())

```

```
import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())  # Run both tasks concurrently

asyncio.run(main())
```
