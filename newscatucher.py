import requests
import json
news=input("which type of news you want ")

url=f"https://newsapi.org/v2/everything?q={news}&from=2023-02-04&sortBy=publishedAt&apiKey=a6aa0f3b992e4f7d83bc463578a6806f"
r=requests.get(url)
all_news=json.loads(r.text)
text=0
for i in all_news["articles"]:
    print(i["title"].upper(),"\n",i["description"],"\n","-"*130)
    
    new_url=i['urlToImage']
    k=requests.get(new_url)
    with open(f"{text}","wb") as fo:
        fo.write(k.content)
    fo.close()
    text+=1
