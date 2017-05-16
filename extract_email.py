from selenium import webdriver
import re
import time

chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('http://www.fiberscope.net/contacts')

doc = driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for email in emails:
    print (email)

time.sleep(4)
driver.close()