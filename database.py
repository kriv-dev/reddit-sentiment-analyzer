import psycopg2
from config import DATABASE_URL

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_results (
            id SERIAL PRIMARY KEY,
            subreddit TEXT,
            post_id TEXT UNIQUE,
            title TEXT,
            sentiment_label TEXT,
            sentiment_polarity FLOAT,
            score INTEGER,
            timestamp BIGINT,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def save_result(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sentiment_results 
            (subreddit, post_id, title, sentiment_label, sentiment_polarity, score, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (post_id) DO NOTHING
    """, (
        data["subreddit"],
        data["post_id"],
        data["title"],
        data["sentiment"]["label"],
        data["sentiment"]["polarity"],
        data["score"],
        data["timestamp"]
    ))
    conn.commit()
    cursor.close()
    conn.close()

def get_sentiment_trends(subreddit, limit=100):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT sentiment_label, COUNT(*) as count
        FROM sentiment_results
        WHERE subreddit = %s
        GROUP BY sentiment_label
        ORDER BY count DESC
        LIMIT %s
    """, (subreddit, limit))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
