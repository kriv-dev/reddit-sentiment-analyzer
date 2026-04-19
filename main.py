import praw
import schedule
import time
from analyzer import analyze_sentiment
from database import save_result
from config import SUBREDDITS, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def create_reddit_client():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

def fetch_and_analyze():
    reddit = create_reddit_client()
    
    for subreddit_name in SUBREDDITS:
        subreddit = reddit.subreddit(subreddit_name)
        
        for post in subreddit.hot(limit=50):
            sentiment = analyze_sentiment(post.title)
            save_result({
                "subreddit": subreddit_name,
                "post_id": post.id,
                "title": post.title,
                "sentiment": sentiment,
                "score": post.score,
                "timestamp": post.created_utc
            })
            
        print(f"Processed {subreddit_name}")

def run_scheduler():
    schedule.every(1).hours.do(fetch_and_analyze)
    print("Scheduler started. Fetching every hour.")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    run_scheduler()
