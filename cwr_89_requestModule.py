import requests
from bs4 import BeautifulSoup
'''r=requests.get("https://www.codewithharry.com")
print(r.text)'''
'''url="https://jsonplaceholder.typicode.com/posts"
data={'title':'Ronit',
      'body':'Bhai',
      'userId':1025}
headers={
    'content-type':'application/json;charset=UTF-8'}
response=requests.post(url,headers=headers,json=data)
print(response.text)'''
r=requests.get("https://www.codewithharry.com/blogpost/django-cheatsheet/")
#print(r.text)
soup=BeautifulSoup(r.text,'html.parser')
#print(soup.prettify())
for heading in soup.find_all('h2'):
    print(heading.text)