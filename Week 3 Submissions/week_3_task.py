from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

service = Service(excecutable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://students.iitk.ac.in/gymkhana/")
driver.implicitly_wait(5)
driver.maximize_window()


tabs=["About","Councils","Cells","Fests","Senate"]
# links = driver.find_elements(By.XPATH, "//a[contains(text(),'tabs']") 
original_tab = driver.current_window_handle
with open("gymkhana_data",'w',encoding='utf-8') as data_file:
    for tab in tabs:
        links = driver.find_elements(By.XPATH,f"//a[contains(text(),'{tab}')]") 

        print(tab)
        links[0].click()
       
        # driver.implicitly_wait(5)
        body=driver.find_element(By.XPATH, "//body" )
        for word in body.get_attribute("innerText").split(' '):
            if(re.match('^[a-zA-Z0-9\.\ ]*$',word)):
                data_file.write(word+" ")
        data_file.write('\n')

        time.sleep(2)
    links = driver.find_elements(By.XPATH,f"//a[contains(text(),'President')]")
    links[0].click()
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(5)
    body=driver.find_element(By.XPATH, "//body" )
    for word in body.get_attribute("innerText").split(' '):
        if(re.match('^[a-zA-Z0-9\.\ ]',word)):
            data_file.write(word+" ")
        
    driver.close()
    driver.switch_to.window(original_tab)
    links = driver.find_elements(By.XPATH,f"//a[contains(text(),'Riwayat')]")
    links[0].click()
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(5)
    body=driver.find_element(By.XPATH, "//body" )
    for word in body.get_attribute("innerText").split(' '):
        if(re.match('^[a-zA-Z0-9\.\ ]',word)):
            data_file.write(word+" ")
    driver.close()
    driver.switch_to.window(original_tab)
       

    time.sleep(5)
    
    
driver.quit()