import requests
import re


def extract_phone_numbers(url):
    response = requests.get(url)
    if response.status_code == 200:
        phone_numbers = re.findall(r'\(\d{3}\) \d{3}-\d{4}', response.text)
        return phone_numbers
    else:
        print(f"Failed to retrieve content. Status Code: {response.status_code}")
        return []


url = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'

result = extract_phone_numbers(url)

print(result)
