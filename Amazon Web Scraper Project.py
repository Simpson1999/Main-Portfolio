#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[2]:


#Connecting to Amazon and pulling the data

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find('span',{'class':'a-offscreen'}).get_text()


print(title)
print(price)


# In[3]:


#Cleaning Up Data
price = price.strip()[1:]

title = title.strip()
print(title)
print(price)


# In[4]:


import datetime

today = datetime.date.today()

print(today)


# In[5]:


import csv

header = ['Title', 'Price', 'Date']
data = [title, price,today]

#with open('AmznWebScraperData.csv', 'w', newline='', encoding='UTF8') as f:
    #writer = csv.writer(f)
    #writer.writerow(header)
    #writer.writerow(data)


# In[6]:


import pandas as pd

df = pd.read_csv(r'C:\Users\stephensimpson.CORP\AmznWebScraperData.csv')

print(df)


# In[7]:


#appending data to csv

with open('AmznWebScraperData.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[8]:


#combining
def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find('span',{'class':'a-offscreen'}).get_text()
    
    price = price.strip()[1:]

    title = title.strip()
    
    import datetime
    
    today = datetime.date.today()
    
    import csv
    
    header = ['Title', 'Price', 'Date']
    data = [title, price,today]

    with open('AmznWebScraperData.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
    


# In[ ]:


#run after set time
while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'C:\Users\stephensimpson.CORP\AmznWebScraperData.csv')

print(df)


# In[ ]:


#Email for price change
def send_mail():
    server = smtplib.SMTP_SSL('steviesimps23.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('9957182@gmail.com','Keprac18')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Stephen, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        '9957182@gmail.com',
        msg
     
    )

