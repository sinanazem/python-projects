import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

def github_check(username):
    url = f'https://github.com/{username}'
    response = requests.get(url)
    if '404' in str(response):
        return False
    return True

def scrape_followers(username):
    followers_response = requests.get(f'https://github.com/{username}?tab=followers')
    followers_soup = BeautifulSoup(followers_response.text)
    followers_list = [i.text for i in followers_soup.select('#user-profile-frame .Link--secondary')]
    return followers_list

def scrape_following(username):
    try:
        # Python 2
        from urllib2 import urlopen
    except ImportError:
        from urllib.request import urlopen
    from lxml import etree

    url =  f"https://github.com/{username}?tab=following"
    response = urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    following_list = [i.text for i in tree.xpath('//*[@class="Link--secondary pl-1"] | //*[@class="Link--secondary"]')]
    return following_list



# Banner
banner = Image.open('github_images.jpeg')
st.image(banner)
st.title('Check Github')
st.write('Check followers and following on Github')

github_username = st.text_input('Please Insert Your Github Username:')

if github_check(github_username):
    following_list = scrape_following(github_username)
    followers_list = scrape_followers(github_username)
    no_f = [i for i in following_list if i not in followers_list]
    st.warning(f'Wellcome {github_username} :grinning:')
    st.write(f'This People dont follow you in Github: \n {no_f}')
else:
    st.warning(f' Username{github_username} Not Found! :pensive:')