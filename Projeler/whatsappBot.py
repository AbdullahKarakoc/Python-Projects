from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

with open('messages.txt', 'r', encoding= 'utf-8') as messages:
    messagelist= list()
    text= messages.read()
    messagelist = text.split('\n')
    
def start():
    flag = False
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://web.whatsapp.com/')
    input('QR kodu okuttuysanız bir tuşa basıp enterlayın')
    message_area = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    while   True:
        message_area.click()
        wp_source = driver.page_source
        soup = bs(wp_source,'lxml')
        search = soup.find_all('div',{'class': ['ggj6brxn gfz4du6o r7fjleex lhj4utae le5p0ye3 _11JPr selectable-text copyable-text']})
        try:
            online = search[0].span.txt  
            print(online)
            if (online in ['çevrimiçi','online']) and flag == False:
                print('online')
                msgToSend=messagelist[random.randint(0,len(messagelist)-1)]
                message_area.send_keys(msgToSend)
                message_area.send_keys(Keys.ENTER)
                flag = True
            elif online not in ['çevrimiçi','online']:
                print("Şu an da çevrim dışı")
                flag = False
        except:
            print('Şu an da çevrimdışı')
            flag = False
            
        time.sleep(2)
        
        
start()

