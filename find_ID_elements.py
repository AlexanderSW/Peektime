from selenium import webdriver

chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('http://www.fiberscope.net/contacts')

ids = driver.find_elements_by_xpath('//*[@id]')

for ii in ids:
    print(ii.get_attribute('id'))

driver.close()