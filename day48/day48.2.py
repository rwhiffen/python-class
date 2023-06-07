# Rich Whiffen - 4/16/2023
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 48 - using Selenium 

# Wikipedia

from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By  #not sure why this is needed but it is

chrome_driver = "/Users/RWhiff000/Applications/chromedriver_mac_arm64/chromedriver"
chrome_service = fs.Service(executable_path=chrome_driver)

driver = webdriver.Chrome(service=chrome_service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

print(article_count.text)