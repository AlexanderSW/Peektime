import time
from selenium import webdriver
chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://admin.peektime.com/")

driver.find_element_by_xpath("""//*[@id="login"]/div/div/div[2]/form/div[3]/button""").click()
time.sleep(3)

try:
    driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[1]/ul/li/i18n')
    print ('Test PASSED: Enter your login')

except Exception as e:
    print ("Exception found",format(e))

driver.find_element_by_name("login").send_keys("rabotapiter21@gmail.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_xpath("""//*[@id="login"]/div/div/div[2]/form/div[3]/button""").click()
time.sleep(3)

try:
    driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[2]/ul/li/i18n')
    print ('Test PASSED: Enter your password')

except Exception as e:
    print ("Exception found",format(e))

driver.find_element_by_name("password").send_keys("210785ap")
driver.find_element_by_xpath("""//*[@id="login"]/div/div/div[2]/form/div[3]/button""").click()

time.sleep(2)
driver.close()