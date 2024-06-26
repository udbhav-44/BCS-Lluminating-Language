from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
import time
from datetime import datetime


chrome_options= Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')
# chrome_options.add_argument("--incognito")

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://spo.iitk.ac.in/about")
time.sleep(5)

# heading=driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div[1]/div[1]/p").text
# print(heading)
# #why Recruit from iitk
# why_heading=driver.find_element("xpath","/html/body/div/div[3]/div[1]/div[2]/div/div/div[1]").text
# print(why_heading)

# for i in range(1,7):
#     title=driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div[2]/div/div/div[2]/div/div[{}]/div[1]".format(i)).text
#     content=driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div[2]/div/div/div[2]/div/div[{}]/div[2]".format(i)).text
#     print(title, ":-")
#     print(content)
# message_title=driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div[3]/div[4]/div[1]/div/div[2]/h1").text
# print(message_title)
# read_more=driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div[3]/div[4]/div[1]/div/div[2]/div/a")
# read_more.click()
# message=driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div/div[2]/div").text
# print(message)
# title=driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div").text
# print(title , ":-")
# messgage=driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div/div[2]/div").text
# print(messgage)

# samvardhan=driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div/div[1]").text
# print(samvardhan , ":")
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div/div[2]").text)
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[1]/div[2]/div[2]/div").text)
# print("Why Participate?")
# for i in range(1,8):
#     title=driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[3]/div/div[{}]/div[1]".format(i)).text
#     content=driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[3]/div/div[{}]/div[2]".format(i)).text
#     print(title, ":-")
#     print(content)
# print("\n")
# print("Target Participants")
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[5]/div").text)
# print("\n")
# print("Event Details")
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[10]/div").text)


#for companies
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div/div[1]").text)
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[1]/div/div[2]").text)
# print("Procedure :")
# for i in range(1,13):
#     print(driver.find_element("xpath", "//html/body/div/div[3]/div[2]/div/div[1]/div/div/div/div/div/div[{}]".format(i)).text)
# print("\n")
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[3]/div/h1").text)
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[3]/div/div/ol").text)
# print("\n")
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[5]/div/h1").text)
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[5]/div/div/ol").text)
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[3]/div/div/ol").text)
# print("\n")
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[7]/div/h1").text)
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[7]/div/div/ul").text)
# print("\n")
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[9]/div/h1").text)
# print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[9]/div/div/div/div").text)


print("About IIT Kanpur :")
print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[2]/div[1]").text)

print("Academics at IIT Kanpur :")
print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[4]/div[1]").text)
for i in range(1,10):
    print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[5]/div[{}]".format(i)).text)
print("\n")

print("Research and Development :")
print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[7]/div[1]").text)
print("\n")
print("Alumni :")
print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[10]").text)
print("\n")
print("Faculty :")
print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[12]/div[1]").text)
print("\n")
print("Students' Life and Activities :")
print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[14]").text)
print("\n")
print("Student Innovation at IIT Kanpur :")
print(driver.find_element("xpath", "/html/body/div/div[3]/div[2]/div/div[19]").text)

















