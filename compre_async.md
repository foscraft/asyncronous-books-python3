List comprehensions in Python are a concise way to create lists by applying an expression to each item in an iterable. While list comprehensions are traditionally used for synchronous code, you can also use asynchronous programming with them to create lists of results from asynchronous tasks. Here are some complex examples of list comprehensions with asynchronous programming in Python using the `asyncio` library:

1. **Asynchronous Web Page Fetching**:

   This example uses a list comprehension to fetch multiple web pages concurrently using `asyncio` and `aiohttp`:

   ```python
   import asyncio
   import aiohttp

   async def fetch_url(url):
       async with aiohttp.ClientSession() as session:
           async with session.get(url) as response:
               return await response.text()

   async def main():
       urls = ["https://example.com", "https://google.com", "https://python.org"]
       pages = await asyncio.gather(*(fetch_url(url) for url in urls))
       page_lengths = [len(page) for page in pages]
       print(page_lengths)

   asyncio.run(main())
   ```

   In this example, the list comprehension `(fetch_url(url) for url in urls)` creates a list of asynchronous tasks for fetching URLs concurrently.

2. **Asynchronous Parallel Processing**:

   You can use list comprehensions to parallelize processing of data with async tasks. Here's an example of processing a list of numbers concurrently:

   ```python
   import asyncio

   async def process_number(number):
       await asyncio.sleep(1)  # Simulate some processing
       return number * 2

   async def main():
       numbers = [1, 2, 3, 4, 5]
       doubled_numbers = await asyncio.gather(*(process_number(num) for num in numbers))
       print(doubled_numbers)

   asyncio.run(main())
   ```

   This code applies the `process_number` coroutine to each number in the list concurrently.

3. **Filtering and Transforming Data**:

   You can use list comprehensions to filter and transform data asynchronously. Here's an example of fetching data and filtering it concurrently:

   ```python
   import asyncio
   import aiohttp

   async def fetch_and_filter_url(url, keyword):
       async with aiohttp.ClientSession() as session:
           async with session.get(url) as response:
               data = await response.text()
               if keyword in data:
                   return url
               return None

   async def main():
       urls = ["https://example.com", "https://google.com", "https://python.org"]
       keyword = "Python"
       filtered_urls = await asyncio.gather(*(fetch_and_filter_url(url, keyword) for url in urls))
       print([url for url in filtered_urls if url])

   asyncio.run(main())
   ```

   This code fetches URLs and filters them based on whether a keyword is found in the fetched content.

These examples demonstrate how list comprehensions can be combined with asynchronous programming to efficiently process and transform data concurrently. This approach can be especially useful when dealing with I/O-bound tasks or network operations.