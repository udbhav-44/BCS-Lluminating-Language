from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


chrome_options= Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://search.pclub.in/")
time.sleep(5)

Batch_bar=driver.find_element('xpath', '/html/body/div/div/div[2]/div/div[1]/div/div/div/div')
Batch_bar.click()
time.sleep(2)
Y23=driver.find_element('xpath', '/html/body/div[2]/div[3]/ul/li[15]')
Y23.click()
time.sleep(2)

close=driver.find_element('xpath', '/html/body/div[2]/div[1]')
close.click()
time.sleep(1)

Programme=driver.find_element('xpath', '/html/body/div/div/div[2]/div/div[4]/div/div/div/div')
Programme.click()
time.sleep(2)
BTech=driver.find_element('xpath', '/html/body/div[2]/div[3]/ul/li[9]')
BTech.click()
BS=driver.find_element('xpath', '/html/body/div[2]/div[3]/ul/li[2]')
BS.click()

close=driver.find_element('xpath', '/html/body/div[2]/div[1]')
close.click()

#Extracting Student Data
Student_names=[]
Student_branch=[]
Student_RollNo=[]
Student_img=[]

for i in range(1,1209):
    try:
        name=driver.find_element('xpath','/html/body/div/div/div[3]/div[2]/div[{}]/div[2]/p[1]'.format(i)).text
    except:
        name=""
    Student_names.append(name)
    try:
        Branch=driver.find_element('xpath', '/html/body/div/div/div[3]/div[2]/div[{}]/div[2]/p[2]'.format(i)).text
    except:
        Branch=''
    Student_branch.append(Branch)
    try:
        RollNo=driver.find_element('xpath', '/html/body/div/div/div[3]/div[2]/div[{}]/div[2]/p[3]'.format(i)).text
    except:
        RollNo=''
    Student_RollNo.append(RollNo)
    try:
        # Find the div element
        div_element = driver.find_element('xpath', '/html/body/div/div/div[3]/div[2]/div[{}]/div[1]'.format(i))

        # Get the value of the style attribute
        style_attribute = div_element.get_attribute('style')

        # Extract the desired URL from the style attribute
        desired_url = style_attribute.split('url("')[2].split('")')[0]

        print(desired_url)
    except:
        desired_url=""
    Student_img.append(desired_url)
    print(Student_names)
data={'Student Name':Student_names,'Student Branch':Student_branch,'Student Roll NO.':Student_RollNo, 'Student Photo': Student_img}
df=pd.DataFrame(data)
df.to_csv('output.csv', index=False)
print('done')


#/html/body/div/div/div[3]/div[2]/div[1027]/div[1]
