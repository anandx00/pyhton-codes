import requests
import json

# data={"username":"anand","password":"anand700776108"}
# k=requests.post("https://httpbin.org/post",data)
# user={"hello":"annd"}
# passwd=700761008
# # k=requests.post("https://httpbin.org/post",user)
# p=requests.get("https://httpbin.org/basic-auth/annd/7007761008")

# print(p.status_code)
# print(json.loads(p.text))

url = "https://httpbin.org/basic-auth/anand/7007761008"
username = "anand"
password = "7007761008"

# Provide the username and password for basic authentication
auth_credentials = (username, password)

# Make the request with authentication
response = requests.get(url, auth=auth_credentials)

print(response.status_code)
 
url="https://httpbin.org/bearer"
data="anand"
username={
  "Authorization": f"Bearer {data}",
}
bearer=requests.get(url,headers=username)
print(bearer.status_code)


url2 = "https://httpbin.org/digest-auth/auth/anand/7007761008/MD5"
data2 = {
    
    "qop":"auth"
}
data1=(username,password)

auth_md5 = requests.get(url2,headers=data2,auth=data1)
print(auth_md5.status_code)

url="https://httpbin.org/image/jpeg"
k=requests.get(url)
print(k.status_code)
with open("anand.jpeg",'wb') as an:
    an.write(k.content)
an.close()