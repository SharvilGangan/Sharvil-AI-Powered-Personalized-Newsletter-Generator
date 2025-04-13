# Main.py

from fetcher import fetch_articles
from classifier import categorize_article
from matcher import load_user_profiles, match_articles_to_user
from newsletter_generator import generate_newsletter


# Mapping of sources to their RSS URLs
SOURCE_URLS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "Wired Tech": "https://www.wired.com/feed/category/tech/latest/rss",
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/technology-lab",
    "MIT Tech Review": "https://www.technologyreview.com/feed/",
    "Bloomberg": "https:TechCrunch//www.bloomberg.com/feed/podcast/etf-report.xml",
    "Financial Times": "https://www.ft.com/?format=rss",
    "Forbes": "https://www.forbes.com/technology/feed/",
    "CoinDesk": "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "ESPN": "https://www.espn.com/espn/rss/news",
    "BBC Sport": "https://feeds.bbci.co.uk/sport/rss.xml",
    "Sky Sports F1": "https://www.skysports.com/rss/12040",
    "The Athletic": "https://theathletic.com/feed/",
    "Variety": "https://variety.com/feed/",
    "Rolling Stone": "https://www.rollingstone.com/music/music-news/feed/",
    "Billboard": "https://www.billboard.com/feed/",
    "Hollywood Reporter": "https://www.hollywoodreporter.com/t/feed/",
    "NASA": "https://www.nasa.gov/rss/dyn/breaking_news.rss",
    "Science Daily": "https://www.sciencedaily.com/rss/all.xml",
    "Nature": "https://www.nature.com/nature.rss",
    "Ars Technica Science": "https://feeds.arstechnica.com/arstechnica/science"
}

if __name__ == "__main__":
    # Ask user for their name
    user_name = input("Enter your name: ").strip()

    # Load user profiles
    users = load_user_profiles()
    user_profile = next((u for u in users if u['name'].lower() == user_name.lower()), None)

    if not user_profile:
        print(f"User '{user_name}' not found. Please check the name and try again.")
        exit()

    articles = []

    print(f"\n📰 Fetching articles for: {user_profile['name']} ({user_profile['tagline']})\n")

    # Fetch up to 5 articles per preferred source
    for source in user_profile['preferred_sources']:
        url = SOURCE_URLS.get(source)

        if not url:
            print(f"⚠️ Source '{source}' has no RSS feed URL mapped. Skipping.\n")
            continue

        source_articles = fetch_articles(url)[:5]  # Limit to 5
        print(f"✅ Fetched {len(source_articles)} articles from {source}")

        # Categorize each article
        for article in source_articles:
            article['category'] = categorize_article(article)

        articles.extend(source_articles)

    if not articles:
        print("\n⚠️ No articles found for the selected sources. Exiting.")
        exit()

    # Match articles to user's interests
    personalized = match_articles_to_user(user_profile, articles)

    # Generate the newsletter
    generate_newsletter(user_profile['name'], personalized)

    print(f"\n🎉 Newsletter successfully generated for {user_profile['name']}!")
