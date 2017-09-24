from urllib import request,parse,error,response
from bs4 import BeautifulSoup
import re
import requests

payload={'key1':'value1','key2':'value2'}
ret= requests.post('http://httpbin.org/post',payload)
print("#No.0001:")
print(ret.text)

url='https://www.baidu.com/'

req = request.Request(url)
response = request.urlopen(req)
print("#No.1==>type of response:")
content = response.read()
con1 =response.readlines()
con2= response.info()
con3 = response.getcode()
con4 = response.geturl()
print(content)
print(con1,"\n",con2,"\n",con3,"\n",con4,"\n")

url2 ='http://blog.csdn.net/ritterliu/article/details/70243112'
req2 = request.Request(url2)
response2 = request.urlopen(req2)
content2 = BeautifulSoup(response2.read(),"html5lib")

print("#No.2==>",content2.title)
print("#No.3==>",content2.find_all(name='h1'))

namelist = content2.find_all(name = 'img')
print("#No.4==>")
for name in namelist:
    print(name)


print('分割线：\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

url3 ='http://www.nipic.com/photo/xiandai/index.html'
req3 = request.Request(url3)
response3 = request.urlopen(req3)
content3 = BeautifulSoup(response3.read(),"html5lib")

print("#No.5==>",content3.title)
print("#No.6==>",content3.find_all(name='h1'))

namelist = content3.find_all(name = 'img')
print("#No.7==>")
for name in namelist:
    print(name)

#构造一个正则表达式"http\:\/\/img84\.nipic\.com\/file\/.+\/.+\.jpg"，  过滤图片
namelist2 = content3.find_all(name = 'img',attrs={"src":re.compile("http\:\/\/img84\.nipic\.com\/file\/.+\/.+\.jpg")})
print("#No.8==>")
for name2 in namelist2:
    print(name2)
    request.urlretrieve(url=name2['src'],filename=name2['alt']+'.jpg')