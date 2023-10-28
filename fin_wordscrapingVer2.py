from bs4 import BeautifulSoup
import requests
import os
from google.colab import drive

# Google Driveをマウント
drive.mount('/content/drive')

# ウェブページのURLを指定
url = 'https://example.com/'

# ウェブページからデータを取得
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# <tbody> タグを探す
tbody_tags = soup.find_all('tbody')

# ファイル名の数字を決定
directory_path = '/content/drive/My Drive/example'
existing_files = os.listdir(directory_path)
existing_numbers = [int(filename.split('_')[-1].split('.')[0]) for filename in existing_files if filename.startswith('finland_word_')]
next_number = max(existing_numbers, default=-1) + 1

# データを2つセットでカンマ区切りのテキストファイルに保存
with open(f'{directory_path}/finland_word_{next_number}.txt', 'w', encoding='utf-8') as file:
    for tbody in tbody_tags:
        rows = tbody.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 3:
                data1 = columns[1].get_text() 
                data2 = columns[2].get_text() 
                file.write(f"{data1},{data2}\n")

print(f'ファイルを {directory_path} に保存しました。')
