from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://iitk.ac.in/dora/alumni-profile")

field = ["Academic","Entrepreneurship","Government-Services","Industry"]
alumni_num = 4

def get_details(i, j):
    try:
        link_xpath = f"//*[@id='{field[i]}']/div/div[{j+3}]/div/div/h5/a"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link_xpath)))
        link = driver.find_element(By.XPATH, link_xpath)
        link.click()
        text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "text-justify"))).text
        driver.back()
        return text
    except Exception as e:
        print(f"Error occurred while getting details: {e}")
        return None

with open('text.txt','a') as f:
    for i in range(4):
        link = driver.find_element(By.XPATH,f"/html/body/section/div[1]/div[2]/div/div/div[1]/a[{i+1}]")
        driver.execute_script("arguments[0].click();", link)
        time.sleep(3)
        for j in range(alumni_num):
            text = get_details(i,j)
            f.write(text)

time.sleep(5)
driver.quit()