import asyncio
from twikit import Client
import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
# Initialize client
client = Client('en-US')

# Define the main asynchronous function
async def main():
    # Log in using the provided credentials
    await client.login(
        auth_info_1=os.getenv("MY_USERNAME"),
        auth_info_2=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD")
    )
    
    # Search for tweets after a successful login
    tweets = await client.search_tweet('Python', 'Latest', count=1000)
    tweets_data = []

    # Print out the tweet details
    for tweet in tweets:
        
        tweet_dict = {
            "full_name":tweet.user.name,
            "text":tweet.text,
            "reply_count":tweet.reply_count,
            "favorite_count":tweet.favorite_count,
            "retweet_count":tweet.retweet_count,
            "created_at":tweet.created_at,
            "profile_image_url":tweet.user.profile_image_url,
            "username":tweet.user.screen_name,
            "view_count": tweet.view_count,
            "url": "https://x.com/m_ashrafy/status/"+ str(tweet.id),
            }
        
        tweets_data.append(tweet_dict)

    
    # Write the tweet data to a JSON file
    with open(Path(".").resolve() / "data" / 'tweets.json', 'w', encoding="utf-8") as json_file:
        json.dump(tweets_data, json_file, indent=4, ensure_ascii=False)

# Use this method if running in an environment with an existing loop
try:
    loop = asyncio.get_running_loop()
    loop.run_until_complete(main())
except RuntimeError:
    asyncio.run(main())
