from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

chromedriver_path = "D:\webscrap\chromedriver.exe"
output_file_path = "D:\webscrap\profinfo.txt"


service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)


driver.get("https://iitk.ac.in/new/iitk-faculty")
driver.implicitly_wait(5)
driver.maximize_window()

# Function to clean and process text
def clean_text(text):
    return " ".join([word for word in text.split() if re.match(r'^[a-zA-Z0-9\.\ ]*$', word)])

# Open a file to save the extracted text
with open(output_file_path, 'w', encoding='utf-8') as data_file:
    total_words = 0  
    
    # Find all department toggle elements
    department_toggles = driver.find_elements(By.XPATH, "//div[@class='jwts_toggleControlContainer']//a")

    for toggle in department_toggles:
        if total_words >= 2000:
            break  
        
        try:
            # Expand the department section
            driver.execute_script("arguments[0].scrollIntoView();", toggle)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(toggle)).click()
            time.sleep(2)  

            
            department_name = toggle.find_element(By.XPATH, ".//span[@class='jwts_toggleControlTitle']").text
            data_file.write(f"Department: {department_name}\n")
            faculty_details = driver.find_elements(By.XPATH, "//div[@class='jwts_toggleContent']//p")

            for detail in faculty_details:
                if total_words >= 2000:
                    break  

                text = detail.get_attribute("innerText")
                cleaned_text = clean_text(text)

                words = cleaned_text.split()
                data_file.write(" ".join(words) + " ")
                total_words += len(words)

            data_file.write("\n")
            
            # Collapse the department section (if necessary)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(toggle)).click()
            time.sleep(1)  

        except Exception as e:
            print(f"Error occurred while processing department '{department_name}': {e}")

    time.sleep(5)

driver.quit()

