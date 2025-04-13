# Matcher.py

import json

def load_user_profiles(path=r'D:\AI Newsletter Generator\users\user_profiles.json'):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def match_articles_to_user(user_profile, articles):
    matched = []
    interests = [interest.lower() for interest in user_profile['interests']]
    preferred_sources = [source.lower() for source in user_profile['preferred_sources']]
    
    # Map user interests to categories
    interest_categories = set()
    for interest in interests:
        if any(word in interest.lower() for word in ["movie", "film", "cinema", "tv", "show", "celebrity", "music", "book"]):
            interest_categories.add("Entertainment")
        if any(word in interest.lower() for word in ["tech", "ai", "program", "cyber", "blockchain"]):
            interest_categories.add("Technology")
        if any(word in interest.lower() for word in ["finance", "market", "crypto", "economics"]):
            interest_categories.add("Finance")
        if any(word in interest.lower() for word in ["sport", "football", "basketball", "soccer", "olympics"]):
            interest_categories.add("Sports")
        if any(word in interest.lower() for word in ["science", "space", "physics", "bio", "energy"]):
            interest_categories.add("Science")

    for article in articles:
        article_source = article.get('source', '').lower()
        article_category = article.get('category', '')
        text = f"{article.get('title', '')} {article.get('summary', '')}".lower()
        
        # Check if article is from preferred source
        source_match = any(preferred in article_source for preferred in preferred_sources)
        
        if source_match:
            # Match by exact interest keywords
            keyword_match = any(interest in text for interest in interests)
            
            # Match by category
            category_match = article_category in interest_categories
            
            if keyword_match or category_match:
                matched.append(article)

    # Log matched articles
    print(f"Matched articles for {user_profile['name']}:")
    for a in matched:
        print(f" - {a['title']} ({a['source']})")
    
    return matched
