import requests
import json

words = requests.get('https://random-word-api.herokuapp.com/word?number=10')
words = words.json()
print("API:", words)
words.sort()
print("API organizada:",words)