import requests

response = requests.get('https://723poil.github.io/web1/1.html')

response.text
print(response.text)
