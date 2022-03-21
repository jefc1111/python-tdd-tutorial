from selenium import webdriver

driver_path = '/usr/bin/chromedriver'
brave_path = '/usr/bin/brave'
option = webdriver.ChromeOptions()
option.binary_location = brave_path
browser = webdriver.Chrome(executable_path=driver_path, options=option)

browser.get('http://localhost:8000')

assert 'Django' in browser.title
