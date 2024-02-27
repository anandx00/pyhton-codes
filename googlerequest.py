import requests
api_key="AIzaSyAXQdjyqu7V2sqjXUTiDqHOlBuODGkmJSk"
cx = "846c90bdcb4684d42"
query =input("enter your query")


def google_search(query, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cx,
        'q': query
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    # print(data)
    print(response.content)

    # Handle the search results
    if 'items' in data:
        for item in data['items']:
            print(item['title'], '-', item['link'])
    else:
        print("No results found.")


    api_key = "AIzaSyAXQdjyqu7V2sqjXUTiDqHOlBuODGkmJSk"
    

# google_search(query, api_key, cx)


def wikipedia_content_download(topic):
    url=f"https://en.wikipedia.org/api/rest_v1/page/pdf/{topic}"
    k=requests.get(url,params={"topic":topic})
    print(k.status_code)
   
    name=input("ENTER THE NAME WHICH YOU WANT TO SAVE")
    print(k.content)
    with open(name+".pdf","wb+") as ad:
        ad.write(k.content)
    ad.close

    
wikipedia_content_download(input("enter which you want to search"))