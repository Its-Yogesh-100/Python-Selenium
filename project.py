from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# to initialize the web browser for chrome
driver = webdriver.Chrome()
# to search the query using the driver.get
query='laptop'
#creating the file
file=0
for i in range(1,20):
    driver.get(f'https://www.amazon.in/s?k={query}&page={i}&crid=1YRU0X283B2X2&sprefix=laptop%2Caps%2C257&ref=nb_sb_noss_2')

    # to get the multiple elements find_elements(By.class_name)
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    # print(elem.text)
    # print(elem.get_attribute('outerHTML'))

    print(f'Total elements found {len(elems)}')

    for elem in elems:
        d=elem.get_attribute('outerHTML')
        with open(f"data/{query}_{file}.html",'w',encoding='utf-8') as f:
            f.write(d)
            file+=1
        
    time.sleep(1)
driver.close()  