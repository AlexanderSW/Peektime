from selenium import webdriver
import time

chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://admin.peektime.com/")

driver.find_element_by_name("login").clear()
driver.find_element_by_name("login").send_keys("rabotapiter21@gmail.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("210785ap")
driver.find_element_by_xpath("""//*[@id="login"]/div/div/div[2]/form/div[3]/button""").click()
time.sleep(2)
driver.find_element_by_xpath("""//*[@id="header"]/header/ul[1]/li/div[4]/a""").click()
time.sleep(2)
driver.find_element_by_xpath("""//*[@id="dashboard"]/div[3]/label[2]""").click()
time.sleep(2)
driver.find_element_by_xpath("""//*[@id="aww-toolbar-window"]/div/div[3]""").click()
time.sleep(2)
