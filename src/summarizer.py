
# summarizer.py

import ollama

def get_enhanced_summary(article):
    """
    Generate a refined 4-5 sentence summary of an article using the Ollama LLM.
    Adds defensive checks and fallback.
    """
    try:
        title = article.get("title", "No Title Provided")
        content = article.get("summary", "No Content Provided")
        
        prompt = (
            "Summarize the following news article in a minimum of 100 to 150 words. "
            "Directly start with the summary content. DO NOT INCLUDE 'Sure, here is the summary'. "
            f"Title: {title}\n"
            f"Content: {content}\n\n"
            "Summary:"
        )

        response = ollama.chat(
            model="gemma:2b",
            messages=[
                {"role": "system", "content": "You are a concise, professional summarization assistant."},
                {"role": "user", "content": prompt}
            ],
            options={"num_ctx": 4096}
        )

        summary = response.get("message", {}).get("content")
        return summary if summary else content

    except Exception as e:
        print(f"[ERROR] Summarization failed for article '{article.get('title', 'Unknown Title')}': {e}")
        # Fallback to plain summary or placeholder
        return article.get("summary", "Summary not available.")

