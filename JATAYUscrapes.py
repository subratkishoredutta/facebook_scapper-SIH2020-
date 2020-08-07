# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:33:23 2020

@author: Asus
"""

import requests
import random
import location as lc
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
path='C:\Program Files (x86)\chromedriver.exe'
from ID import username, password

class FaceBookBot():

    def __init__(self):
        self.driver = webdriver.Chrome(path)

    def login(self,username, password):
        self.driver.get("https://www.facebook.com/login")

        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

        sleep(2)
        
       


##TIMELINE

    
def TimelinePost(link):
    bot = FaceBookBot()
    bot.login(username,password)
    bot.driver.get(link)
    for i in range(1,15):
        bot.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(3)
    page = bot.driver.page_source
    soup=BeautifulSoup(page,"html.parser")
    all_posts=soup.find_all('div',class_='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q')#_5rgn #qzhwtbm6 knvmm38d #kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q
    all_dates=soup.find_all('a',class_='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw')#_5rgn #qzhwtbm6 knvmm38d #kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q
    posts=[]
    dates=[]
    for post in all_posts:
        posts.append(post.text)
    for date in all_dates:
        dates.append(date.text)
    return posts,dates

#qzhwtbm6 knvmm38d
def getPOSTS(URL):
    posts,_=TimelinePost(URL)
    print(len(posts))
    import pandas as pd
    data =  pd.DataFrame({'Post':posts})
    data.to_csv('POSTs.csv')
    return posts



def getPOSTdateANDtime(URL):
    import location as lc
    import pandas as pd
    LOC=lc.loadLOC_data()
    _,DAP =  TimelinePost(URL)
    count=0
    for date in DAP:
        L=[]
        for i in date:
            L.append(i.isnumeric())
        if True in L:
            count+=1
    fromDate=''
    M=[]
    for i in date:
        M.append(i.isnumeric())       
    if True in L:
        fromDate = DAP[-1]
    else:
        fromDate = DAP[-2]
    toDate=DAP[0]
    
    print("from "+str(fromDate)+" to "+str(toDate)+ " we have "+str(count)+" number of posts.")
    finalDate=[]
    trackdates=[]
    trackPlaces=[]
    n=0
    for date in DAP:
        
        L=[]
        for i in date:
            L.append(i.isnumeric())
        if True in L:
            finalDate.append(date)
        elif date in LOC:
            trackPlaces.append(date)
            trackdates.append(DAP[n-1])
        n+=1
        
    dates=pd.DataFrame({'POSTdates':finalDate})
    dates.to_csv('POSTdates.csv')
    trackLOC = pd.DataFrame({'date':trackdates,'location':trackPlaces})
    trackLOC.to_csv('track.csv')
    return finalDate,trackLOC
##single post specfic 
    
def getReactions(URL):
    bot = FaceBookBot()
    bot.login(username,password)
    link = URL.replace('www','mbasic',1)
    bot.driver.get(link)
    page = bot.driver.page_source
    soup=BeautifulSoup(page,"html.parser")
    L1=soup.find_all('a',class_='_45m8')#_5rgn #qzhwtbm6 knvmm38d #kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q
    link='https://mbasic.facebook.com'+str(L1[0].attrs['href'])
    bot.driver.get(link)   
    page = bot.driver.page_source
    soup=BeautifulSoup(page,"html.parser")
    L2=soup.find_all('a',class_='z')
    link='https://mbasic.facebook.com'+str(L2[0].attrs['href'])
    link=link.replace('10','10000',1)
    bot.driver.get(link)
    page = bot.driver.page_source
    soup=BeautifulSoup(page,"html.parser")
    LC=soup.find_all('h3',class_='bj')
    liked_by=[]
    for name in LC:
        liked_by.append(name.text)
    print(str(len(liked_by))+" people have reacted to this post")
    return liked_by
    
def getpost(URL):
    bot = FaceBookBot()
    bot.login(username,password)
    link = URL.replace('www','mbasic',1)
    bot.driver.get(link)
    page = bot.driver.page_source
    soup=BeautifulSoup(page,"html.parser")
    L=soup.find_all('div',class_='_2vj8')
    #_5rgn #qzhwtbm6 knvmm38d #kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q
    caption=''
    for t in L:
        caption = t.text
    print(caption)
    return caption

def getDate(URL):
    bot = FaceBookBot()
    bot.login(username,password)
    link = URL.replace('www','mbasic',1)
    bot.driver.get(link)
    page = bot.driver.page_source
    soup=BeautifulSoup(page,"html.parser")
    L=soup.find_all('div',class_='_2vja mfss fcg')
    date=''
    for i in L:
        string = i.text
    temp=string.split('·')
    date=temp[0]
    print(date)
    return date

def getcomments(URL):
    bot= FaceBookBot()
    bot.login(username,password)
    link = URL.replace('www','mbasic',1)
    bot.driver.get(link)
    page = bot.driver.page_source
    soup=BeautifulSoup(page,"html.parser")
    L=soup.find_all('div',class_='_14ye')
    comments=[]
    for i in L:
        comments.append(i.text)
        
    M=soup.find_all('a',class_='_1s79 _52jh')
    commentor=[]
    for j in M:
        commentor.append(j.text)
        
    return comments,commentor

    
URL='https://www.facebook.com/sauraja.sarkar'
    
 
    
getPOSTdateANDtime(URL)    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    