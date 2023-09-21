"""_summary_
    Using Asyncio, you can structure your code so subtasks are defined as coroutines and
    allows you to schedule them as you please, including simultaneously.
    Coroutines contain yield points where we define possible points where a
    context switch can happen if other tasks are pending, but will not if no other task is pending.
    A context switch in asyncio represents the event loop yielding the flow of control from one coroutine to the next.
    In the process below, we run 3 async tasks that query Reddit separately, extract and print the JSON.
    We leverage aiohttp which is a http client library ensuring even the HTTP request runs asynchronously.
    Returns:
        _type_: _description_
"""
import signal
import sys
import asyncio
import aiohttp
import json

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)

async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()

async def get_reddit_top(subreddit, client):
    data1 = await get_json(
        client,
        f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5',
    )

    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(f'{str(score)}: {title} ({link})')

    print(f'DONE: ,  {subreddit}\n')

def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

asyncio.ensure_future(get_reddit_top('python', client))
asyncio.ensure_future(get_reddit_top('programming', client))
asyncio.ensure_future(get_reddit_top('compsci', client))
loop.run_forever()