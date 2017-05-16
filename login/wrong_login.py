import time
from selenium import webdriver

chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://admin.peektime.com/")
time.sleep(3)
driver.find_element_by_name("login").clear()
driver.find_element_by_name("login").send_keys("rabotapiter21.gmail.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("210785ap")
driver.find_element_by_xpath("""//*[@id="login"]/div/div/div[2]/form/div[3]/button""").click()
time.sleep(3)
driver.find_element_by_xpath("""//*[@id="login"]/div/div/div[2]/form/div[1]/div/p/i18n""")

try:
    driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[1]/div/p/i18n')
    print ('Test PASSED: Wrong login')

except Exception as e:
    print ("Exception found",format(e))

time.sleep(2)
driver.close()
