# -*- coding:utf-8 -*-
import requests

session = requests.Session()
# definecd header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
with open('url_list.txt', 'r') as f:
    for line in f:
        url = line.strip()
        try:
            response = session.get('https://' + url, verify=True, headers=headers, stream=True)
            # response = requests.head(url, allow_redirects=True)
            if response.status_code == 200:
                print(f'OK {url} has valid SSL certificate.')
            else:
                response = session.get('http://' + url, verify=True, headers=headers, stream=True)
                if response.status_code in (301, 302):
                    print(f'OK {url} redirects to {response.url}')
                else:
                    print(f'NG {url} does not redirect to HTTPS')
            
        except Exception as e:
            print(f'Error {url} : {e}')