"""
web_scraping_demo.py - Scrape quotes, authors, and tags using requests and BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    headers = {"User-Agent": "PythonStudentScraper/1.0"}

    print(f"Fetching {url} ...")
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quote container blocks (<div class="quote">)
    quote_blocks = soup.find_all("div", class_="quote")
    print(f"Found {len(quote_blocks)} quotes on the page.\n")

    results = []
    for block in quote_blocks:
        # Extract quote text (<span class="text">)
        text = block.find("span", class_="text").get_text(strip=True)

        # Extract author name (<small class="author">)
        author = block.find("small", class_="author").get_text(strip=True)

        # Extract tags (<a class="tag">)
        tag_elements = block.find_all("a", class_="tag")
        tags = [t.get_text(strip=True) for t in tag_elements]

        results.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    return results


if __name__ == "__main__":
    quotes = scrape_quotes()

    # Display the first 3 scraped quotes
    for i, item in enumerate(quotes[:3], 1):
        print(f"{i}. \"{item['quote']}\"")
        print(f"   - Author: {item['author']}")
        print(f"   - Tags  : {', '.join(item['tags'])}\n")
