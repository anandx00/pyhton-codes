import requests
import json
r=requests.get("https://edition.cnn.com/")
k=r.content

print(k,r.status_code)