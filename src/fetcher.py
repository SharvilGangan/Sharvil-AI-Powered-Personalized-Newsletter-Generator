# fetcher.py

import feedparser
def fetch_articles(rss_url):
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries:
        article = {
            'title': entry.get('title'),
            'summary': entry.get('summary', ''),
            'link': entry.get('link'),
            'published': entry.get('published', ''),
            'source': feed.feed.get('title', 'Unknown Source')
        }
        articles.append(article)

    # Log fetched articles
    print(f"Fetched articles from {rss_url}:")
    for a in articles:
        print(f" - {a['title']} ({a['source']})")
    return articles



# import feedparser

# def fetch_articles(rss_url):
#     feed = feedparser.parse(rss_url)
#     articles = []
#     for entry in feed.entries:
#         articles.append({
#             'title': entry.get('title'),
#             'summary': entry.get('summary', ''),
#             'link': entry.get('link'),
#             'published': entry.get('published', ''),
#             'source': feed.feed.get('title', 'Unknown Source')
#         })
#     return articles


# if __name__ == "__main__":
#     url = "https://techcrunch.com/feed/"
#     articles = fetch_articles(url)
#     for a in articles[:3]:
#         print(f"{a['title']} ({a['source']})\n{a['link']}\n")
