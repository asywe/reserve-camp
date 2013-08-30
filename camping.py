import datetime
import sys
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

while True:
  now = datetime.datetime.now()
  if now.minute == 53 :
    break

length.submit()

emailTextBox = driver.find_element_by_id("AemailGroup_1733152645")
emailTextBox.send_keys(sys.argv[1])
pwtb = driver.find_element_by_id("ApasswrdGroup_704558654")
pwtb.send_keys(sys.argv[2])
submitButton = driver.find_element_by_id("submitForm_submitForm")
submitButton.click()
