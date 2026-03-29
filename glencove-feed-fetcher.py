import requests
from bs4 import BeautifulSoup

URL = "https://visitglencove.com/"

def fetch_articles():
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except Exception as e:
        print("Error fetching site:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    # Adjust selectors depending on your site structure
    for link in soup.find_all("a", href=True):
        title = link.get_text(strip=True)
        href = link["href"]

        if title and "glen" in href.lower():
            articles.append((title, href))

    return articles[:10]


def main():
    print("Latest from Visit Glen Cove:\n")

    articles = fetch_articles()

    if not articles:
        print("No articles found.")
        return

    for i, (title, link) in enumerate(articles, 1):
        print(f"{i}. {title}")
        print(f"   {link}\n")


if __name__ == "__main__":
    main()
