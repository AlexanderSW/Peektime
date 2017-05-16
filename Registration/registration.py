from selenium import webdriver
from  selenium.webdriver.support.select import Select
import time
chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://admin.peektime.com/")
driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/div/p/a/small/i18n').click()
driver.find_element_by_xpath('//*[@id="login"]/small/div/div/div[2]/form/section/div/div[1]/div/input').send_keys('podobulkin21@yandex.ru')
select = Select(driver.find_element_by_xpath('//*[@id="login"]/small/div/div/div[2]/form/section/div/div[2]/div/select'))
select.select_by_value('1')
driver.find_element_by_xpath('//*[@id="login"]/small/div/div/div[2]/form/section/div/div[3]/div/input').send_keys('Alexander')
driver.find_element_by_xpath('//*[@id="login"]/small/div/div/div[2]/form/section/div/div[4]/div/input').send_keys('Podobulkin')
driver.find_element_by_xpath('//*[@id="login"]/small/div/div/div[2]/form/section/div/div[5]/div/input').send_keys('+38(050)111-11-11')
driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[5]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login"]/small/div/div/div[2]/form/div/p/button/i18n').click()
time.sleep(2)
driver.close()








