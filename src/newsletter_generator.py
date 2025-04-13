# newsletter_generator.py

from collections import defaultdict
from summarizer import get_enhanced_summary
import textwrap
import os
import json
from pdf_generator import clean_and_generate_pdf

# Mapping interests to article categories
INTEREST_CATEGORY_MAP = {
    "Global markets": "Finance",
    "fintech": "Finance",
    "cryptocurrency": "Finance",
    "economics": "Finance",
    "startups": "Technology",
    "AI": "Technology",
    "cybersecurity": "Technology",
    "blockchain": "Technology",
    "programming": "Technology",
    "Football": "Sports",
    "F1": "Sports",
    "NBA": "Sports",
    "Olympic sports": "Sports",
    "esports": "Sports",
    "Movies": "Entertainment",
    "celebrity news": "Entertainment",
    "TV shows": "Entertainment",
    "music": "Entertainment",
    "books": "Entertainment",
    "Space exploration": "Science",
    "biotech": "Science",
    "physics": "Science",
    "renewable energy": "Science"
}

# Get allowed categories for user based on their interests
def get_user_categories(user_name, profiles):
    user = next((u for u in profiles if u['name'] == user_name), None)
    if not user:
        return []

    categories = set()
    for interest in user['interests']:
        category = INTEREST_CATEGORY_MAP.get(interest)
        if category:
            categories.add(category)

    return list(categories)

# Generate newsletter file
def generate_newsletter(user_name, articles, user_profiles_path="D://AI Newsletter Generator//users//user_profiles.json", output_dir=r"D:\AI Newsletter Generator\output"):
    # Load user profiles
    with open(user_profiles_path, 'r') as f:
        profiles = json.load(f)

    # Get the user's allowed categories
    allowed_categories = get_user_categories(user_name, profiles)

    if not allowed_categories:
        print(f" Warning: No valid categories found for {user_name}. Check user profile interests.")
        return

    # Filter articles based on allowed categories
    relevant_articles = [a for a in articles if a.get('category') in allowed_categories]

    # If there are no relevant articles, still generate a placeholder newsletter
    os.makedirs(output_dir, exist_ok=True)
    safe_name = user_name.replace(" ", "_")
    output_path = os.path.join(output_dir, f"newsletter_{safe_name}.md")

    # Grouping articles by category (only relevant ones)
    grouped = defaultdict(list)
    for article in relevant_articles:
        article['enhanced_summary'] = get_enhanced_summary(article).strip()
        category = article.get('category', 'General')
        grouped[category].append(article)

    # Log matched articles
    print(f"\nMatched articles for {user_name}: {len(relevant_articles)} found")
    for category, items in grouped.items():
        print(f" - {category}: {len(items)} articles")

    # Writing newsletter
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Personalized Newsletter for {user_name}\n\n")
        f.write(f"Hi {user_name}, here are your curated articles for today:\n\n")

        if not relevant_articles:
            f.write(" No relevant articles matched your interests today. Stay tuned for the next update!\n")
            print(f" No articles found for {user_name}. Newsletter generated with no content.")
            return

        # Highlights - Top 3 recent articles
        sorted_articles = sorted(relevant_articles, key=lambda x: x.get('published', ''), reverse=True)
        highlights = sorted_articles[:3]

        if highlights:
            f.write("## Highlights\n\n")
            for article in highlights:
                wrapped_summary = textwrap.fill(article['enhanced_summary'], width=120)
                f.write(f"- [{article['title']}]({article['link']})\n")
                f.write(f"  > {wrapped_summary}\n\n")
            f.write("---\n\n")

        # Grouped categories
        for category, items in grouped.items():
            f.write(f"## {category}\n\n")
            for article in items:
                wrapped_summary = textwrap.fill(article['enhanced_summary'], width=120)
                f.write(f"- [{article['title']}]({article['link']})\n")
                f.write(f"  > {wrapped_summary}\n\n")

        f.write("\n---\n")
        f.write("End of newsletter.\n")

    print(f"✅ Newsletter generated for {user_name}: {output_path}")
    clean_and_generate_pdf(output_dir, os.path.join(output_dir, "pdf"))
