from flask import Flask, jsonify, render_template
from database import get_sentiment_trends

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/trends/<subreddit>")
def trends(subreddit):
    data = get_sentiment_trends(subreddit)
    return jsonify({
        "subreddit": subreddit,
        "trends": [{"label": row[0], "count": row[1]} for row in data]
    })

if __name__ == "__main__":
    app.run(debug=True)
