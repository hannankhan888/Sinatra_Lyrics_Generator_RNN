import os
import csv

data_path = r'data'
filename = 'Lyrics_FrankSinatra'
txt_filepath = os.sep.join([data_path, filename + '.txt'])
csv_filepath = os.sep.join([data_path, filename + '.csv'])

if os.path.exists(txt_filepath):
    os.remove(txt_filepath)

with open(txt_filepath, 'w', encoding='utf-8') as f:
    with open(csv_filepath, newline='', encoding='utf-8') as c:
        reader = csv.reader(c, delimiter=',')
        for i, row in enumerate(reader):
            if row and i > 0:
                f.write(row[-1].strip())
