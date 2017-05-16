import time
from selenium import webdriver
chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://admin.peektime.com/")
time.sleep(2)
driver.find_element_by_class_name("pull-right").click()
time.sleep(2)
driver.find_element_by_xpath("""//*[@id="login"]/small/div/div/div[2]/form/div[1]/input""").clear()
driver.find_element_by_xpath("""//*[@id="login"]/small/div/div/div[2]/form/div[1]/input""").send_keys("rabotapiter21gmail.com")
driver.find_element_by_xpath("""//*[@id="login"]/small/div/div/div[2]/form/div[2]/p/button""").click()
time.sleep(2)
driver.find_element_by_xpath("""//*[@id="login"]/small/div/div/div[2]/form/div[1]/div/p/i18n""")
print ('Test PASSED')

time.sleep(2)
driver.close()