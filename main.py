from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import pandas as pd 
import numpy as np 
import time 
import csv 
from selenium import webdriver
import telegram_send
import datetime  
import csv 

if __name__ == "__main__":

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("user-agent=[Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36]")
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
    driver =webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)

    while(True):
        now = datetime.datetime.now()
        if(now.hour in [0,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]):

            driver.get('https://www.sahibinden.com/ozel-ders-verenler-lise-universite')
            soup = bs(driver.page_source, 'html.parser')
            results = soup.select('#searchResultsTable > tbody')
            ilan_idleri = [994177898, 981519161]
            first_20_data = []
            for ilan in range(1,21):
                first_20_data.append(soup.find_all('tr')[ilan]["data-id"])
            
            with open("data.csv","a") as f:
                writer = csv.writer(f)
                writer.writerow(first_20_data)
                f.close()
        
            for myIlan in ilan_idleri:
                if(str(myIlan) not in first_20_data[:5]):
                
                    if(myIlan == 994177898):
                        telegram_send.send(messages=["Fatih  ilan ilk 5 sirada degil!"])
                    if(myIlan == 981519161):
                        telegram_send.send(messages=["Kadir ilan ilk 5 sirada degil!"])


        time.sleep(900)
    
        
    

    

    



    



#928771751


#time.sleep(30000)


