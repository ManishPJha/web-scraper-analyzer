import asyncio
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Proxy list (replace with a larger list or use a proxy pool service)
proxies = [
    "http://3.126.147.182:80",
    "http://92.50.76.42:8080",
    "http://154.65.39.7:80",
    # Add more proxies here
]


def get_random_proxy():
    """Get a random proxy address."""
    return random.choice(proxies)


def get_random_user_agent():
    """Get a random user-agent."""
    ua = UserAgent()
    return ua.random


async def scrape_page(session, url):
    """Scrape a single page."""
    headers = {"User-Agent": get_random_user_agent()}

    proxy = (
        get_random_proxy()
    )  # include proxy to header when required proxies to scrap the page

    try:
        async with session.get(url, headers=headers, timeout=10) as response:
            response.raise_for_status()
            soup = BeautifulSoup(await response.text(), "html.parser")
            return soup
    except Exception as e:
        logger.error(f"Error scraping {url}: {e}")
        return None


async def extract_urls_from_sitemap(session, sitemap_url):
    """Extract URLs from a sitemap."""
    try:
        async with session.get(sitemap_url) as response:
            response.raise_for_status()
            soup = BeautifulSoup(await response.text(), "lxml-xml")
            urls = [loc.text for loc in soup.find_all("loc")]
            return urls
    except Exception as e:
        logger.error(f"Error fetching sitemap {sitemap_url}: {e}")
        return []


async def scrape_website_from_sitemap(session, sitemap_url, limit):
    """Scrape multiple pages from a sitemap."""
    scraped_data = []

    urls = await extract_urls_from_sitemap(session, sitemap_url)
    logger.info(f"Found {len(urls)} URLs in the sitemap.")

    if limit > 0:
        urls = urls[:limit]

    for url in urls:
        logger.info(f"Scraping {url}...")
        soup = await scrape_page(session, url)
        if soup:
            data = {
                "url": url,
                "title": soup.title.string if soup.title else "No Title",
                "content": soup.get_text(),
                "html": soup.prettify(),
            }
            scraped_data.append(data)

        # Add a random delay between requests (2-5 seconds)
        await asyncio.sleep(random.uniform(2, 5))

    return scraped_data
