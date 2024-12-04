import streamlit as st
import streamlit.components.v1 as components
import json
from pathlib import Path


BASE_DIR = Path(".").resolve()

st.image(str(BASE_DIR / "src/app/static" / "pytopia-text.webp"), width=210)
col1, col2 = st.columns(2)
with col1:
    st.markdown("# What our users say about us?")
    
with col2:
    
    st.image(str(BASE_DIR / "src/app/static/" / "review.webp"), width=310)

def create_card(author_name, author_handle, avatar_url, tweet_content, comment_count, retweet_count, like_count):
    # Define the HTML and CSS with the injected data
    tweet_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            .tweet-container {{
                width: 100%;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                padding: 10px;
                margin: 10px 0; /* Adjust margin to reduce gap */
            }}
            .tweet-header {{
                display: flex;
                align-items: center;
            }}
            .avatar {{
                border-radius: 50%;
                width: 50px;
                height: 50px;
                margin-right: 10px;
            }}
            .tweet-author {{
                font-weight: bold;
            }}
            .tweet-handle {{
                color: gray;
                margin-left: 5px;
            }}
            .tweet-content {{
                margin-top: 10px; /* Adjust */
            }}
            .tweet-footer {{
                display: flex;
                justify-content: space-between;
                margin-top: 10px; /* Adjust */
                color: gray;
            }}
            .tweet-footer div {{
                display: flex;
                align-items: center;
            }}
            .tweet-footer div i {{
                margin-right: 5px;
            }}
        </style>
    </head>
    <body>
        <div class="tweet-container">
            <div class="tweet-header">
                <img class="avatar" src="{avatar_url}" alt="Avatar">
                <div>
                    <span class="tweet-author">{author_name}</span> 
                    <span class="tweet-handle">{author_handle}</span>
                </div>
            </div>
            <div class="tweet-content">
                {tweet_content}
            </div>
            <div class="tweet-footer">
                <div>
                    <i class="fa-regular fa-comment"></i> {comment_count}
                </div>
                <div>
                    <i class="fa-solid fa-retweet"></i> {retweet_count}
                </div>
                <div>
                    <i class="fa-regular fa-heart"></i> {like_count}
                </div>
                <div>
                    <i class="fa-solid fa-share"></i>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    components.html(tweet_html, height=200, scrolling=False)  # Adjust height if needed

# Load tweets from JSON file
with open(str(BASE_DIR / "data" / "tweets.json"), 'r') as file:
    tweets = json.load(file)

# Display tweets in two columns per row
for i in range(0, len(tweets), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(tweets):
            tweet = tweets[i + j]
            with cols[j]:
                create_card(author_name=tweet["full_name"],
                            author_handle=tweet["username"],
                            avatar_url=tweet["profile_image_url"],
                            tweet_content=tweet["text"],
                            comment_count=tweet["reply_count"],
                            retweet_count=tweet["retweet_count"],
                            like_count=tweet["favorite_count"])
