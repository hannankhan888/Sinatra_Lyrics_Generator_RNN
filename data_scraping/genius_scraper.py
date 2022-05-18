import os

import lyricsgenius
import requests
from dotenv import load_dotenv

# set up lyricsgenius
load_dotenv()
genius = lyricsgenius.Genius(os.getenv('GENIUS_ACCESS_TOKEN'),
                             timeout=20, retries=3)

# extract all songs with the artist id 824 (Frank Sinatra)
artist_id = 824
try:
    artist = genius.search_artist(artist_id=artist_id, artist_name="Frank Sinatra",
                                  get_full_info=False)
except requests.exceptions.Timeout:
    artist.save_lyrics()
artist.save_lyrics()

# option 2: custom scraping via json
# https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/07-Genius-API.html
