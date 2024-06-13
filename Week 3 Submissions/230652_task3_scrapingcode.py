from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(excecutable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.ecelliitk.org")

xpaths = [
    '//*[@id="home"]/div[2]/div/div/div/h1',
    '//*[@id="about"]/div/div/div/h3',
    '//*[@id="about"]/div/div/div/p',
    '//*[@id="services"]/div[3]/div',
    '//*[@id="services"]/div[4]/div/div[1]/div',
    '//*[@id="services"]/div[4]/div/div[2]',
    '//*[@id="services"]/div[4]/div/div[3]/div',
    '//*[@id="services"]/div[4]/div/div[4]/div',
    '//*[@id="services"]/div[4]/div/div[5]/div',
    '//*[@id="services"]/div[4]/div/div[6]',
    '//*[@id="magazine"]/div[1]/div/div/h1',
    '//*[@id="magazine-wrap"]/div[2]/p'
]

for xpath in xpaths:
    element = driver.find_element(By.XPATH, xpath)
    print(element.get_attribute("innerText").split(' '))

driver.get("https://www.ecelliitk.org/esummit/")
xpaths = [
    '/html/body/div[23]/div[2]/div[3]/div[1]',
    '/html/body/div[23]/div[2]/div[5]/div[2]',
    '//*[@id="comp1"]/div/div[1]',
    '//*[@id="comp2"]/div/div[1]',
    '//*[@id="comp3"]/div/div[1]',
    '//*[@id="comp4"]/div/div[1]',
    '//*[@id="comp5"]/div/div[1]',
    '//*[@id="comp6"]/div/div[1]'
]

for xpath in xpaths[:2]:
    element = driver.find_element(By.XPATH, xpath)
    print(element.get_attribute("innerText").split(' '))

print('COMPETITIONS')

for xpath in xpaths[2:]:
    element = driver.find_element(By.XPATH, xpath)
    print(element.get_attribute("innerText").split(' '))

driver.get("https://www.ecelliitk.org/YEC/")

yes1 = driver.find_element(By.XPATH,'//*[@id="about"]/div/div[1]/p')
print(yes1.get_attribute("innerText").split(' '))
yes2 = driver.find_element(By.XPATH,'//*[@id="about"]/div/div[2]/p')
print(yes2.get_attribute("innerText").split(' '))

driver.get("https://www.ecelliitk.org/ca/")

cac = driver.find_element(By.XPATH,'//*[@id="about"]/div[1]/div')
print(cac.get_attribute("innerText").split(' '))

driver.get("https://iitkcombinator.com/")

xpaths = [
    '//*[@id="incent"]/div[2]/div/div[1]/div/div/div/div/p',
    '//*[@id="incent"]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/p',
    '//*[@id="incent"]/div[2]/div/div[2]/div[1]/div[2]/div/div/div/p',
    '//*[@id="incent"]/div[2]/div/div[2]/div[1]/div[3]/div/div/div/p'
]

for xpath in xpaths:
    element = driver.find_element(By.XPATH, xpath)
    print(element.get_attribute("innerText").split(' '))

driver.get("https://www.ecelliitk.org/HII/")

hill = driver.find_element(By.XPATH,'//*[@id="overview"]/div')
print(hill.get_attribute("innerText").split(' '))

driver.get("https://www.ecelliitk.org/entreverse/")

xpaths = [
    '//*[@id="about"]/div/div/div/p',
    '//*[@id="contact"]/div[3]/div[1]/div[1]/div',
    '//*[@id="contact"]/div[3]/div[1]/div[2]/div',
    '//*[@id="contact"]/div[3]/div[2]',
    '//*[@id="competitions"]/div[1]'
]

for xpath in xpaths:
    element = driver.find_element(By.XPATH, xpath)
    print(element.get_attribute("innerText").split(' '))

driver.get("https://www.ecelliitk.org/startup-service-provision/")

serprov = driver.find_element(By.XPATH,'//*[@id="about"]/div/p')
print(serprov.get_attribute("innerText").split(' '))

driver.get("https://www.ecelliitk.org/esquare/")

xpaths = [
    '//*[@id="about"]/div/div/div/p',
    '//*[@id="competitions"]/div[3]/div/div[1]/div',
    '//*[@id="competitions"]/div[3]/div/div[2]/div'
]

for xpath in xpaths:
    element = driver.find_element(By.XPATH, xpath)
    print(element.get_attribute("innerText").split(' '))

driver.get("https://www.ecelliitk.org/tedx/")

tedx1 = driver.find_element(By.XPATH,'/html/body/main/div[2]/section[2]/div/h3')
print(tedx1.get_attribute("innerText").split(' '))

time.sleep(5)

driver.quit()