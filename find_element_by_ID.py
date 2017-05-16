from selenium import webdriver
import time

chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('http://www.fiberscope.net/contacts')

try:
    driver.find_element_by_id('main')
    print ('Test PASS: ID found')

except Exception as e:
    print ("Exception found",format(e))

time.sleep(2)
driver.close()