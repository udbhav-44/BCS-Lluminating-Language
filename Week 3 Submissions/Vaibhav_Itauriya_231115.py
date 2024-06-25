from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Define the path to the ChromeDriver executable
service = Service(exececutable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.iitk.ac.in/futurestudents/blog/")

try:
    extracted_texts = []

    # Loop for the first section
    for i in range(1, 13):
        try:
            link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"/html/body/div[2]/div/div[1]/div[1]/div/div/ul/li[{i}]/a[1]")
                )
            )
            link.click()

            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

            # Get all window handles
            all_window_handles = driver.window_handles
            original_window_handle = driver.current_window_handle

            # Switch to the new window
            new_window_handle = next(handle for handle in all_window_handles if handle != original_window_handle)
            driver.switch_to.window(new_window_handle)

            try:
                main_content = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "#mainContent > div.q-box.qu-borderAll.qu-borderRadius--small.qu-borderColor--raised.qu-boxShadow--small.qu-bg--raised > div > div > div > div > div > div:nth-child(1) > div.q-box.qu-mb--tiny > div > span > span > a > span")
                    )
                )
            except (TimeoutException, NoSuchElementException):
                driver.close()
                driver.switch_to.window(original_window_handle)
                continue

            # Extract text from the main content
            paragraphs = main_content.find_elements(By.CSS_SELECTOR, "span")
            content = "\n".join([p.text for p in paragraphs])
            extracted_texts.append(content)

            try:
                main_content = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "#mainContent > div.q-box.qu-borderAll.qu-borderRadius--small.qu-borderColor--raised.qu-boxShadow--small.qu-bg--raised > div > div > div > div > div > div:nth-child(1) > div.q-text > span > span")
                    )
                )
            except (TimeoutException, NoSuchElementException):
                driver.close()
                driver.switch_to.window(original_window_handle)
                continue

            # Extract text from the main content
            paragraphs = main_content.find_elements(By.CSS_SELECTOR, "span")
            content = "\n".join([p.text for p in paragraphs])
            extracted_texts.append(content)

            # Close the new window and switch back to the original window
            driver.close()
            driver.switch_to.window(original_window_handle)

        except (TimeoutException, NoSuchElementException) as e:
            print(f"Exception occurred for link {i}: {e}")

    # Loop for the second section
    for j in range(1, 14):
        for i in range(1,6):
            try:
                link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"/html/body/div[2]/div/div[1]/div[2]/div[{j}]/div/ul/li[{i}]/a[1]")
                    )
                )
                link.click()

                WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

                # Get all window handles
                all_window_handles = driver.window_handles
                original_window_handle = driver.current_window_handle

                # Switch to the new window
                new_window_handle = next(handle for handle in all_window_handles if handle != original_window_handle)
                driver.switch_to.window(new_window_handle)

                
                
                try:
                    main_content = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "#mainContent > div.q-box.qu-borderAll.qu-borderRadius--small.qu-borderColor--raised.qu-boxShadow--small.qu-bg--raised > div > div > div > div > div > div:nth-child(1) > div.q-box.qu-mb--tiny > div > span > span > a > span")
                        )
                    )
                except (TimeoutException, NoSuchElementException):
                    driver.close()
                    driver.switch_to.window(original_window_handle)
                    continue

                # Extract text from the main content
                paragraphs = main_content.find_elements(By.CSS_SELECTOR, "span")
                content = "\n".join([p.text for p in paragraphs])
                extracted_texts.append(content)

                try:
                    main_content = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "#mainContent > div.q-box.qu-borderAll.qu-borderRadius--small.qu-borderColor--raised.qu-boxShadow--small.qu-bg--raised > div > div > div > div > div > div:nth-child(1) > div.q-text > span > span")
                        )
                    )
                except (TimeoutException, NoSuchElementException):
                    driver.close()
                    driver.switch_to.window(original_window_handle)
                    continue

                # Extract text from the main content
                paragraphs = main_content.find_elements(By.CSS_SELECTOR, "span")
                content = "\n".join([p.text for p in paragraphs])
                extracted_texts.append(content)

                # Close the new window and switch back to the original window
                driver.close()
                driver.switch_to.window(original_window_handle)

            except (TimeoutException, NoSuchElementException) as e:
                print(f"Exception occurred for link {j} {i}: {e}")

    # Write the extracted texts to a .txt file
    # Change the directory to save the txt file in your local Device
    with open("C:/Users/vaibh/Courses, Contest or Camps/BCS Summer Project/BCS-Lluminating-Language/Week 3/Thats_IITK_Blogs_extracted_texts.txt", "w", encoding="utf-8") as file:
        for idx, text in enumerate(extracted_texts, start=1):
            file.write(f"{text}\n\n")

finally:
    driver.quit()
