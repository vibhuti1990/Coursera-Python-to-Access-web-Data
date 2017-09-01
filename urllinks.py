#Week 2 : Extracting data with regular Expression
import re
file = open('Actual.txt','r')
data=file.readlines()
num=0
x=[]
for line in data:
    y=re.findall('[0-9]+',line)
    x=x+y
sum=0
for num in x:
    sum=sum+int(num)
print(sum)


#Week 4: Assignment 1 (Adding Numbers by extracting from tags)
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
Count =0
num=0
for tag in tags:
    # Look at the parts of a tag
    Count=Count+1
    #Retrieve strings from span tag and convert it to number
    num=num+int(tag.text)
print('Count: ', Count)
print('Sum: ', num)





#Week 4: Assignemnt 2 (Retrieving Links)
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL: ')
count = input('Enter Count: ')
position = int(input('Enter Position: '))
for i in range(int(count)+1):
        print('Retrieving: %s' %url )
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all of the anchor tags
        tags = soup('a')
        c=0
        for tag in tags:
           c=c+1 
           if(c== position):
             #retrieve all the links
             url= tag.get('href',None)
             

#Week 5: 
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
sum=0
results = tree.findall('.//count')
for items in results:
     sum=sum+ int(items.text)
print(len(results))
print(sum)


#Week 6
#Extracting data from JSON
import urllib.request, urllib.parse, urllib.error
import json
info=[]
url = input('Enter URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
data=info['comments']
sum=0
for items in data:
     sum=sum+ int(items['count'])
print('Count: ', len(data))
print('Sum: ', sum)


#Calling a JSON API
import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
#        print(data)
        continue

    id = js["results"][0]["place_id"]   
    print('Place id  ', id)




           
                    

        
                    
    
