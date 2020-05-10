import aiohttp
import asyncio


async def fetch_async(url):
    async with aiohttp.ClientSession() as session:  # 协程嵌套，只需要处理最外层协程即可fetch_async
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text())  # 因为这里使用到了await关键字，实现异步，所有他上面的函数体需要声明为异步async


tasks = [fetch_async('http://www.baidu.com/'), fetch_async('http://www.cnblogs.com/ssyfj/')]

event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()
