import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup


def get_urls() -> list:
    address = input("Enter the complete website address: ")
    request = requests.get(address)
    soup = BeautifulSoup(request.text, 'html.parser')

    urls = []
    for tag in soup.find_all('a'):
        link = tag.get('href')
        title = tag.get('title')
        if not link or link.startswith('/'):
            pass
        else:
            urls.append({'link': link, 'title': title})

    return urls


async def load_pages(url: dict) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url['link']) as response:
            print(f'Getting {url["link"]}')
            data = await response.text()
            with open(f'./downloads/{url["title"]}.html', 'w') as f:
                f.write(data)
                f.close()
        await session.close()


def main():
    retrieved_urls = get_urls()
    futures = [load_pages(u) for u in retrieved_urls]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))


if __name__ == '__main__':
    main()
