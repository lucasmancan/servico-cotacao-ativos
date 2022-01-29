import requests
import pandas as pd
import numpy as np

url = 'https://www.fundsexplorer.com.br/ranking'
headers = {
    'User-Agent': 
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36'
        ' (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}


def collect():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        df = pd.read_html(response.content, encoding='utf-8')[0]

    df = df.fillna('')
    return df.to_dict('records')


