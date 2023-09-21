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