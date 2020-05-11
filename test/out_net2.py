import aiohttp


async def test_2():
    async with aiohttp.ClientSession() as session:
        async with session.get(test_url, headers=header) as response:
            response.encoding = 'utf8'
