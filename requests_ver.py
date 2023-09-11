import requests

print(requests.__version__)

x = requests.get("https://raw.githubusercontent.com/mark8m/CMPUT404-lab1/main/requests_ver.py")

print(x.text)