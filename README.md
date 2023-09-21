`asyncio` is a Python library that provides support for asynchronous programming using coroutines, tasks, and event loops. Below, I'll explain some of the key methods and functions provided by `asyncio` along with examples:

1. **Creating and Running an Event Loop**:
   - `asyncio.run(coro)`: This function runs the specified coroutine in an event loop.
   
   Example:
   ```python
   import asyncio
   
   async def main():
       print("Hello, asyncio!")
   
   asyncio.run(main())
   ```

2. **Creating Coroutines**:
   - `async def coroutine_name()`: Define asynchronous coroutines using the `async def` syntax.

   Example:
   ```python
   async def greet(name):
       await asyncio.sleep(1)
       print(f"Hello, {name}!")
   ```

3. **Creating Tasks**:
   - `asyncio.create_task(coro)`: Creates a task to run the specified coroutine concurrently.

   Example:
   ```python
   task = asyncio.create_task(greet("Alice"))
   ```

4. **Waiting for Coroutines**:
   - `await coroutine`: Use the `await` keyword to wait for the completion of a coroutine.

   Example:
   ```python
   async def main():
       task1 = asyncio.create_task(greet("Alice"))
       task2 = asyncio.create_task(greet("Bob"))
       await task1
       await task2
   ```

5. **Running Multiple Coroutines Concurrently**:
   - `asyncio.gather(*coros)`: Runs multiple coroutines concurrently and waits for all of them to complete.

   Example:
   ```python
   async def main():
       await asyncio.gather(greet("Alice"), greet("Bob"))
   ```

6. **Sleeping and Delaying Execution**:
   - `await asyncio.sleep(seconds)`: Sleeps (pauses) the execution of a coroutine for the specified number of seconds.

   Example:
   ```python
   async def main():
       print("Start")
       await asyncio.sleep(2)
       print("End")
   ```

7. **Handling Exceptions**:
   - `asyncio.try/catch` blocks or `asyncio.ensure_future(coro)`: Handle exceptions raised within asynchronous code.

   Example:
   ```python
   async def risky_operation():
       raise Exception("Something went wrong")

   async def main():
       try:
           await asyncio.ensure_future(risky_operation())
       except Exception as e:
           print(f"Caught an exception: {e}")
   ```

8. **Using Event Loop with Callbacks**:
   - `asyncio.loop.run_in_executor()`: Run a synchronous function in a separate thread or process and wait for its completion.

   Example:
   ```python
   import asyncio
   
   def blocking_function():
       return "Result from blocking function"
   
   async def main():
       result = await asyncio.to_thread(blocking_function)
       print(result)
   ```

9. **Working with Semaphores**:
   - `asyncio.Semaphore(value)`: Create a semaphore with the specified value. Semaphores are useful for controlling access to a limited resource.

   Example:
   ```python
   async def worker(semaphore):
       async with semaphore:
           print("Working...")
           await asyncio.sleep(1)
           print("Done")

   async def main():
       semaphore = asyncio.Semaphore(2)  # Allow two workers at a time
       await asyncio.gather(worker(semaphore), worker(semaphore))
   ```

10. **Timeouts**:
    - `asyncio.wait_for(coro, timeout)`: Set a timeout for a coroutine, raising `asyncio.TimeoutError` if it doesn't complete within the specified time.

    Example:
    ```python
    async def slow_operation():
        await asyncio.sleep(3)

    async def main():
        try:
            await asyncio.wait_for(slow_operation(), timeout=2)
        except asyncio.TimeoutError:
            print("Operation timed out")
    ```

11. **Cancelling Tasks**:
    - `task.cancel()`: Cancel a running task.

    Example:
    ```python
    async def foo():
        try:
            while True:
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            print("Task foo was cancelled")

    async def main():
        task = asyncio.create_task(foo())
        await asyncio.sleep(3)
        task.cancel()
    ```

12. **Event Handling with Callbacks**:
    - `loop.add_reader(fd, callback)`: Register a callback to be called when there is data available to read on a file descriptor.
    - `loop.add_writer(fd, callback)`: Register a callback to be called when a file descriptor is ready for writing.

    Example (listening for keyboard input):
    ```python
    import asyncio

    def on_keyboard_input():
        data = input("Enter something: ")
        print(f"You entered: {data}")

    def main():
        loop = asyncio.get_event_loop()
        loop.add_reader(0, on_keyboard_input)
        loop.run_forever()

    if __name__ == "__main__":
        main()
    ```

13. **Creating and Using Locks**:
    - `asyncio.Lock()`: Create a lock that can be used to synchronize access to shared resources in concurrent coroutines.

    Example:
    ```python
    async def worker(lock):
        async with lock:
            print("Locked...")
            await asyncio.sleep(1)
            print("Unlocked")

    async def main():
        lock = asyncio.Lock()
        await asyncio.gather(worker(lock), worker(lock))
    ```

Asynchronous programming in Python allows you to write non-blocking, concurrent code that can improve the performance of I/O-bound and network-bound tasks. Python's `asyncio` library is the primary tool for asynchronous programming. Here's an overview of how asynchronous programming works in Python:

1. **Coroutines**: The fundamental building blocks of asynchronous programming in Python are coroutines. These are defined using the `async` keyword and can be thought of as functions that can be paused and resumed at certain points without blocking the entire program. Coroutines are created using the `async def` syntax.

   ```python
   async def my_coroutine():
       # Asynchronous code here
   ```

2. **Event Loop**: To run asynchronous code, you need an event loop, which is responsible for scheduling and executing asynchronous tasks. Python's `asyncio` provides a default event loop.

3. **Asynchronous Functions**: You can use the `await` keyword inside a coroutine to wait for another coroutine, an I/O operation, or a task to complete without blocking the entire program. When `await` is called, the control is returned to the event loop, allowing other tasks to run.

   ```python
   async def foo():
       await asyncio.sleep(1)
       print("Foo completed")

   async def bar():
       await asyncio.sleep(2)
       print("Bar completed")

   async def main():
       task1 = asyncio.create_task(foo())
       task2 = asyncio.create_task(bar())
       await task1
       await task2

   asyncio.run(main())
   ```

4. **Task Management**: You can create tasks to execute coroutines concurrently using `asyncio.create_task()`. These tasks can be awaited or managed using various asyncio functions.

5. **Event Handling**: Asynchronous programming often involves handling events, such as receiving data from a network socket or waiting for user input. You can use the `asyncio` event loop to manage these events efficiently.

Here's a simple example of an asynchronous program that fetches multiple web pages concurrently:

```python
import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://example.com", "https://google.com", "https://python.org"]
    tasks = [fetch_url(url) for url in urls]
    pages = await asyncio.gather(*tasks)
    for url, page in zip(urls, pages):
        print(f"Fetched {len(page)} bytes from {url}")

asyncio.run(main())
```

This code asynchronously fetches web pages from multiple URLs concurrently using `aiohttp`. The `asyncio.gather()` function is used to await multiple coroutines concurrently.

Asyncio is just one way to work with asynchronous programming in Python. There are other libraries like `trio` and `curio` that provide alternative approaches. The choice of library depends on your specific use case and coding style.