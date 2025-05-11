# Code to fetch data from Federal Register API
import requests

def download_data(url, output_file):
    response = requests.get(url)
    with open(output_file, 'wb') as f:
        f.write(response.content)
