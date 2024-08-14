import requests

def fetch_external_data():
    response = requests.get('https://api.example.com/employees')
    return response.json()