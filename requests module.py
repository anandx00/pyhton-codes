import requests
r=requests.get('https://httpbin.org/#/',allow_redirects=False,timeout=3)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
#exceptional allow_redirects it does not allow redirects 
#timeout wait for the website if it responses under that timeout then it return no 
#error

payload = {'key1': 'value1', 'key2': 'value2'}
payload2 = {'key1': 'value1', 'key2': ['value2', 'value3']}
y = requests.get('https://httpbin.org/get', params=payload)


data={"username":"anand","password":"anand700776108"}
k=requests.post("https://httpbin.org/#/HTTP_Methods/post_post/",data)

#to download image
url=input("enter you image url")
m=requests.get(url)
with open ("another.png",'wb') as fd:
    fd.write(m.content)
fd.close()
o=requests.session()
z=o.get('https://httpbin.org/#/')
print(z.request.headers)
# print(z.text)

