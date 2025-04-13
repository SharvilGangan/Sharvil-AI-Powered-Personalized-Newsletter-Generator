# Classifier.py

def categorize_article(article):
    categories = {
        "Technology": [
            "AI", "artificial intelligence", "cybersecurity", "blockchain", "crypto", "startups",
            "programming", "coding", "developer", "robotics", "machine learning", "deep learning",
            "cloud computing", "cloud", "saas", "iaas", "paas", "quantum computing", "software",
            "hardware", "semiconductor", "5G", "web3", "app", "mobile app", "VR", "AR",
            "virtual reality", "augmented reality", "data science", "big data", "databases",
            "internet of things", "IoT", "edge computing", "AI ethics", "AI safety", 
            "open source", "git", "github", "API", "framework", "neural network",
            "algorithm", "python", "java", "javascript", "typescript", "linux", "windows"
        ],

        "Finance": [
            "stocks", "stock market", "bonds", "mutual funds", "hedge fund", "ETF", 
            "cryptocurrency", "bitcoin", "ethereum", "trading", "investments", "portfolio", 
            "NASDAQ", "NYSE", "Dow Jones", "S&P 500", "inflation", "interest rates", 
            "recession", "fintech", "debt", "equity", "startup funding", "venture capital", 
            "private equity", "mergers", "acquisitions", "IPO", "SPAC", "financial markets",
            "exchange rate", "forex", "banking", "federal reserve", "monetary policy", "dividends",
            "yields", "pensions", "tax", "cryptowallet", "stablecoin", "defi", "blockchain",
            "central bank", "GDP", "economic growth", "credit", "budget", "fiscal policy"
        ],

        "Sports": [
            "football", "soccer", "nba", "nfl", "mlb", "fifa", "uefa", "epl", "premier league", 
            "cricket", "icc", "ipl", "tennis", "grand slam", "wimbledon", "olympics", "olympic", 
            "athletics", "marathon", "triathlon", "formula 1", "f1", "motogp", "nascar", "rugby",
            "golf", "pga", "basketball", "baseball", "hockey", "esports", "valorant", "csgo", 
            "dota", "league of legends", "messi", "ronaldo", "neymar", "federer", "nadal", 
            "djokovic", "lebron", "michael jordan", "serena williams", "tom brady", "usain bolt",
            "maradona", "pele"
        ],

        "Entertainment": [
            "movie", "movies", "film", "films", "cinema", "hollywood", "bollywood", "tv", "series", 
            "sitcom", "netflix", "amazon prime", "disney+", "hotstar", "hbo", "paramount+", "hulu",
            "apple tv", "documentary", "drama", "comedy", "thriller", "oscars", "emmys", "grammys",
            "bafta", "red carpet", "blockbuster", "box office", "trailer", "premiere", "festival",
            "coachella", "snl", "succession", "friends", "kardashian", "reality show", "superhero",
            "marvel", "dc comics", "batman", "avengers", "spiderman", "celebrity", "gossip",
            "concert", "music", "album", "single", "track", "playlist", "spotify", "itunes",
            "chart", "billboard", "rolling stone", "variety", "imdb", "performance", "performer",
            "actor", "actress", "singer", "band", "rapper", "pop star", "rock star", "director"
        ],

        "Science": [
            "nasa", "spacex", "esa", "rocket", "space", "black hole", "astronomy", "astrophysics",
            "quantum mechanics", "physics", "chemistry", "biology", "genetics", "neuroscience",
            "biotech", "biotechnology", "ecology", "geology", "meteorology", "paleontology", 
            "climate change", "global warming", "renewable energy", "solar power", "wind power",
            "fusion", "fission", "dna", "rna", "protein", "cell", "virus", "bacteria", "vaccine",
            "pandemic", "epidemic", "covid", "hubble", "james webb", "mars", "moon", "asteroid",
            "meteor", "satellite", "exoplanet", "particle physics", "cern", "lhc", "higgs boson",
            "space station", "iss", "robotics", "ai research", "clinical trials"
        ]
    }

    # Define source-to-category mappings
    source_category_map = {
        # Entertainment sources
        "variety": "Entertainment",
        "billboard": "Entertainment", 
        "rolling stone": "Entertainment",
        "hollywood reporter": "Entertainment",
        "music news": "Entertainment",
        
        # Technology sources
        "techcrunch": "Technology",
        "wired tech": "Technology",
        "ars technica": "Technology",
        "mit tech review": "Technology",
        
        # Finance sources
        "bloomberg": "Finance",
        "financial times": "Finance",
        "forbes": "Finance",
        "coindesk": "Finance",
        
        # Sports sources
        "espn": "Sports",
        "bbc sport": "Sports",
        "sky sports": "Sports",
        "the athletic": "Sports",
        
        # Science sources
        "nasa": "Science",
        "science daily": "Science",
        "nature": "Science",
        "ars technica science": "Science"
    }
    
    # Get source and check if we have a direct category mapping
    source = article.get('source', '').lower()
    
    # Try to categorize by source first
    for source_keyword, category in source_category_map.items():
        if source_keyword in source:
            print(f"Categorized article '{article['title']}' as {category} (based on source)")
            return category
    
    # If source-based categorization fails, fall back to keyword matching
    text = f"{article['title']} {article.get('summary', '')}".lower()
    match_counts = {}

    for category, keywords in categories.items():
        # Count how many keywords appear in the text for each category
        count = sum(keyword.lower() in text for keyword in keywords)
        match_counts[category] = count

    # Select category with maximum keyword hits
    best_category = max(match_counts, key=match_counts.get)

    if match_counts[best_category] > 0:
        print(f"Categorized article '{article['title']}' as {best_category}")
        return best_category
    else:
        print(f"Categorized article '{article['title']}' as General")
        return "General"

