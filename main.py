from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import pandas as pd 
import numpy as np 
import time 
import csv 
from selenium import webdriver



    
    


if __name__ == "__main__":

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("user-agent=[Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36]")
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
    driver =webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
    driver.get('https://www.sahibinden.com/ozel-ders-verenler-lise-universite')
    

    soup = bs(driver.page_source, 'html.parser')
    results = soup.select('#searchResultsTable > tbody')

    # bizim ilanlarin idleri burada olacak 

    ilan_idleri = [928771751, 996891248]

    
    first_20_data = []
    for ilan in range(1,21):
        first_20_data.append(soup.find_all('tr')[ilan]["data-id"])
    
    
    print(first_20_data)
        
    

    

    



    



#928771751


#time.sleep(30000)


