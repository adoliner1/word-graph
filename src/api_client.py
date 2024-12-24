import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DatamuseClient:
    def __init__(self):
        self.base_url = "https://api.datamuse.com"

    def get_synonyms(self, word):
        response = requests.get(f"{self.base_url}/words", params={'rel_syn': word})
        response.raise_for_status()
        return [item['word'] for item in response.json()]

    def get_rhymes(self, word):
        response = requests.get(f"{self.base_url}/words", params={'rel_rhy': word})
        response.raise_for_status()
        return [item['word'] for item in response.json()]

    def get_homophones(self, word):
        response = requests.get(f"{self.base_url}/words", params={'sl': word})
        response.raise_for_status()
        return [item['word'] for item in response.json() if item['score'] > 90]