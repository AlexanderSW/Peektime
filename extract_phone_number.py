from selenium import webdriver
import re
import time

chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('http://www.fiberscope.net/contacts')

doc = driver.page_source

phones = re.findall(r'[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}', doc)
phones = re.findall(r'[\d]{1}[ ][\d]{3}[ ][\d]{3}[ ][\d]{2}[ ][\d]{2}', doc)

for phone in phones:
    print (phones)

time.sleep(4)
driver.close()
