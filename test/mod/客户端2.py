from lxml import etree
import aiohttp
import asyncio

"""
获取外网IP、位置

"""


class PublicIp(object):
    def __init__(self):
        self.out_out_net_position = []

    def get_data(self) -> list:
        """
        返回最终结果
        :return:
        """
        return self.out_out_net_position

    async def fetch_async2(self, url) -> list:
        async with aiohttp.ClientSession() as session:  # 协程嵌套，只需要处理最外层协程即可fetch_async
            headers = {
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/67.0.3396.10 Safari/537.36'
            }
            async with session.get(url, headers=headers) as resp:
                if resp.status == 200:
                    html = await resp.text()  # 因为这里使用到了await关键字，实现异步，所有他上面的函数体需要声明为异步async
                    # print(html)
                    html_emt = etree.HTML(html)
                    code_list: list = html_emt.xpath('//div[@id="result"]//code/text()')
                    # print(code_list)
                    if code_list:
                        self.out_out_net_position = code_list
                        return code_list[:2]
                else:
                    return []

    def main(self):
        tasks = [self.fetch_async2('https://ip.cn')]
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(asyncio.gather(*tasks))
        event_loop.close()


if __name__ == '__main__':
    app = PublicIp()
    app.main()
