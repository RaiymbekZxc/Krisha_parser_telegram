
import aiohttp, bs4


async def get_news():
    new = []
    for i in range(1, 5):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://krisha.kz/prodazha/kvartiry/almaty/?page={i}', verify_ssl = False) as response:
                html = await response.text()
                soup = bs4.BeautifulSoup(html, 'html.parser')
                link = soup.find_all('a', class_='a-card__title')
                for links in link:
                    new.append(f'https://krisha.kz{links.get("href")}')
    return new