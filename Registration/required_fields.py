from selenium import webdriver
from  selenium.webdriver.support.select import Select
import time
chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://admin.peektime.com/")

driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/div/p/a/small/i18n').click()
driver.find_element_by_xpath('//*[@id="login"]/small/div/div/div[2]/form/div/p/button/i18n').click()
driver.find_element_by_xpath('//*[@id="login"]/small/div/div/div[2]/form/section/div[2]/div[1]/div/ul/li/i18n')

driver.close()