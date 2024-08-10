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

- asyncio.as_completed is useful when the order of completion is significant, such as when you need to process results in a particular order (like sorting by delay).


- asyncio.gather collects all results but maintains the order in which the coroutines were started, which does not necessarily reflect the order in which they finish.

# asyncio methods
When working with asynchronous programming in Python using `asyncio`, there are several key methods and functions that you can use to manage asynchronous tasks effectively. Here’s an overview of the most important ones:

### 1. **`async def`**: 
   - This is how you define an asynchronous function (coroutine) in Python. These functions can use `await` to pause execution until the awaited coroutine is done.

   ```python
   async def my_coroutine():
       await asyncio.sleep(1)
       return "Done"
   ```

### 2. **`await`**:
   - This keyword is used to pause the execution of the coroutine until the awaited coroutine completes. It can only be used inside an `async def` function.

   ```python
   result = await my_coroutine()
   ```

### 3. **`asyncio.run()`**:
   - This function is used to run the top-level coroutine and manage the event loop. It’s typically used to execute the main coroutine in a script.

   ```python
   asyncio.run(my_coroutine())
   ```

### 4. **`asyncio.create_task()`**:
   - This function schedules the execution of a coroutine and returns an `asyncio.Task` object. The task runs concurrently with other tasks.

   ```python
   task = asyncio.create_task(my_coroutine())
   ```

### 5. **`asyncio.gather()`**:
   - This function runs multiple coroutines concurrently and waits for all of them to complete. It returns a list of results.

   ```python
   results = await asyncio.gather(my_coroutine(), my_coroutine())
   ```

### 6. **`asyncio.sleep()`**:
   - This coroutine pauses the execution for a specified number of seconds, allowing other tasks to run.

   ```python
   await asyncio.sleep(1)
   ```

### 7. **`asyncio.as_completed()`**:
   - This function returns an iterator that yields tasks as they are completed, allowing you to process results in the order they finish, rather than the order they were started.

   ```python
   for task in asyncio.as_completed([task1, task2]):
       result = await task
   ```

### 8. **`asyncio.wait()`**:
   - This function waits for multiple tasks to complete, with options to wait for all tasks or just the first one to finish. It returns two sets of tasks: completed and pending.

   ```python
   done, pending = await asyncio.wait([task1, task2], return_when=asyncio.ALL_COMPLETED)
   ```

### 9. **`asyncio.shield()`**:
   - This function protects a coroutine from being canceled. If the outer task is canceled, the shielded task will still run to completion.

   ```python
   await asyncio.shield(my_coroutine())
   ```

### 10. **`asyncio.Event`**:
    - This class is used to manage synchronization between coroutines. An `Event` object allows one coroutine to signal an event while others wait for it.

   ```python
   event = asyncio.Event()
   
   async def waiter():
       await event.wait()
       print("Event received!")
   
   async def setter():
       await asyncio.sleep(1)
       event.set()
   
   asyncio.run(asyncio.gather(waiter(), setter()))
   ```

### 11. **`asyncio.Queue`**:
   - This class is used for queueing items in a thread-safe way between producer and consumer coroutines.

   ```python
   queue = asyncio.Queue()
   
   async def producer():
       await queue.put("item")
   
   async def consumer():
       item = await queue.get()
   ```

### 12. **`asyncio.LifoQueue`, `asyncio.PriorityQueue`**:
   - Variations of `asyncio.Queue` for Last-In-First-Out and priority-based queueing, respectively.

### 13. **`asyncio.TimeoutError`**:
   - Raised when an operation times out. You can use it with timeouts to handle tasks that take too long.

   ```python
   try:
       await asyncio.wait_for(my_coroutine(), timeout=1.0)
   except asyncio.TimeoutError:
       print("Timed out!")
   ```

### 14. **`asyncio.run_until_complete()`**:
   - This function was used in older versions of asyncio to run a coroutine until it completed. It has been largely replaced by `asyncio.run()`.

Understanding and using these `asyncio` methods effectively allows you to build robust asynchronous applications in Python, handling concurrent tasks efficiently.
