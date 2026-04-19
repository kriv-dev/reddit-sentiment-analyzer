# reddit-sentiment-analyzer

## Overview
A tool that tracks sentiment trends in Reddit communities over time 
to help understand community health and engagement patterns.

## Features
- Fetches posts/comments from specified subreddits (read-only)
- Runs sentiment analysis on collected text
- Displays trends on a web dashboard
- No user data stored, no posting or voting

## Tech Stack
- Python
- PRAW (Reddit API wrapper)
- NLTK / TextBlob for sentiment analysis
- PostgreSQL for storing results
- Flask for the dashboard

## How It Works
1. App authenticates with Reddit API using OAuth2
2. Fetches recent posts from target subreddits
3. Runs sentiment scoring on titles and comments
4. Stores results in database
5. Dashboard displays trends over time

## Target Subreddits
r/investing, r/stocks, r/wallstreetbets, r/personalfinance

## Setup
(installation instructions here)

## API Usage
This app uses Reddit's API in compliance with their 
terms of service. Read-only access, respects rate limits.
