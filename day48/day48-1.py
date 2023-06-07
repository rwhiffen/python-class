
# Rich Whiffen - 4/16/2023
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 48 - using Selenium 

# the amazon example isn't a good one - too much has changed since she wrote the class

from selenium import webdriver
from selenium.webdriver.common.by import By  #not sure why this is needed but it is

chrome_driver="/Users/RWhiff000/Applications/chromedriver_mac_arm64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.amazon.com/Kelly-Kettle-Trekker-Kit-Lightweight/dp/B095JDG5J6/?_encoding=UTF8&pd_rd_w=xC0U1&content-id=amzn1.sym.08900ed4-dd64-49b1-bce7-2e717defb1aa&pf_rd_p=08900ed4-dd64-49b1-bce7-2e717defb1aa&pf_rd_r=7JCGQ8HMDG44ET3JMKSE&pd_rd_wg=wr8Cn&pd_rd_r=c4eba9ec-605e-4c57-bb70-7ccc5275a656&ref_=pd_gw_ci_mcx_mi")

kettle_price = driver.find_element(By.ID, "attach-base-product-price")

print(kettle_price)
blah = input("type anything + enter to continue: ")
driver.quit()
