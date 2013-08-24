from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.reserveamerica.com/camping/Pfeiffer_Big_Sur_Sp/r/campsiteDetails.do?contractCode=CA&siteId=4491&parkId=120068")

arrivalDate = driver.find_element_by_id("arrivaldate")
arrivalDate.send_keys("Wed Feb 19 2014")

length = driver.find_element_by_id("lengthOfStay")
length.send_keys("2")
length.submit()
length = driver.find_element_by_id("lengthOfStay")
length.submit()

emailTextBox = driver.find_element_by_id("AemailGroup_1733152645")
emailTextBox.send_keys("sywe.abby@gmail.com")
pwtb = driver.find_element_by_id("ApasswrdGroup_704558654")
pwtb.send_keys("google")
submitButton = driver.find_element_by_id("submitForm_submitForm")
submitButton.click()
