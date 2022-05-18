import json
import csv
import os
import re
import pickle

data_path = r'..\data'
filename = 'Lyrics_FrankSinatra'
replacements_filepath = os.sep.join([data_path, 'replacements_dict.pkl'])
json_filepath = os.sep.join([data_path, filename + '.json'])
csv_filepath = os.sep.join([data_path, filename + '.csv'])

punctuation = r"!#$%&'()*\+,-./:;<=>?@\[\]\^'_`{|}~0123456789©Ãààâçöğ˜œ"
brackets = r"\[.*?\]"
braces = r"{.*?}"
parentheses = r"\([^)]*\)"
replacements = {
    ',': '', "'": '', '...': '', ':': '', '..': '', 'unk': '', '-': '', '—': '', '’': '',
    '\n': ' ', 'embed': '', '"': '', '\\': '', '0': '', '1': '', '2': '', '3': '',
    '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', '    ': ' ', '   ': ' ', '  ': ' ',
    '!': '', '#': '', '$': '', '&': '', '*': '', '+': '', '/': '', ';': '', '=': '',
    '@': '', '_': '', '`': '', '|': '', '~': '', '©': '', 'œ': '', '\u2005': '',
    '\u200a': '', '\u200b': '', '\u205f': '', '–': '', '‘': '', '“': '', '”': '', '•': '',
    '…': '', '\u2028': '', '′': '', '€': '', '↗': '', ')': '', '[': '', ']': '', '{': '',
    '}': '', 'Ã': 'A', 'à': 'a', 'á': 'a', 'â': 'a', 'ç': 'c', 'è': 'e', 'é': 'e',
    'ê': 'e', 'ë': 'e', 'í': 'i', 'ñ': 'n', 'ò': 'o', 'ó': 'o', 'ö': 'o', 'ü': 'u',
    'ğ': 'g', '˜': '', 'е': 'e', '¡': '', '¢': '', '¤': '', '­': '', '´': '', '¸': '', '¹': '',
    'ã': '', 'ä': '', 'ą': '', 'ć': '', 'ę': '', 'ł': '', 'ń': '', 'ś': '', 'ż': '', 'ž': '', '‚': '', '抦': '',
    '抰': '', '.': '', '?': '', '(': ''
}

# save replacements dictionary
if os.path.exists(replacements_filepath):
    os.remove(replacements_filepath)
with open(replacements_filepath, 'wb') as f:
    pickle.dump(replacements, f, protocol=pickle.HIGHEST_PROTOCOL)

# load data from json
with open(json_filepath, 'r') as f:
    data = json.load(f)
songs = data['songs']

"""
song_id: songs[n]['id']
title: songs[n]['title]
url: ...['url']
artists: ...['artist_names']
lyrics: ...['lyrics']
"""
if os.path.exists(csv_filepath):
    os.remove(csv_filepath)
# now we can create the .csv of the same name
header = ['song_id', 'title', 'url', 'artists', 'lyrics']
with open(csv_filepath, 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for song in songs:
        lyrics = song['lyrics'].lower()
        lyrics = re.sub(brackets, '', lyrics)
        lyrics = re.sub(braces, '', lyrics)
        lyrics = re.sub(parentheses, '', lyrics)
        lyrics = re.sub(punctuation, '', lyrics)
        lyrics = lyrics[lyrics.find("lyrics") + 6:].strip()
        for k, v in replacements.items():
            lyrics = lyrics.replace(k, v)
        if len(lyrics) >= 100:
            writer.writerow([
                song['id'],
                song['title'],
                song['url'],
                song['artist_names'],
                lyrics
            ])

# only 1079/1085 songs have actual lyrics (len > 100)
