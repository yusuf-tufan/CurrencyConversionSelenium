
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import numpy as np
from print_color import print

chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

#Go to URL
url='https://www.foreks.com/doviz/'
driver.get(url)
sleep(2)

listofcurrencies=['TRY','USD','EUR','CHF','GBP','CAD','AUD','CNY','RUB','CNH','SEK','KWD','PKR','QAR','DKK','SAR','BGN','RON','NOK','IRR','JPY','ZAR','RSD','AED','BYN','TJS','','']
driver.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

#money amount entry and sending
input_value=input('Enter first value: ')
sleep(1)
value1=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/input")
value1.clear()
value1.send_keys(f'{input_value}')
sleep(1)

#currency selection
sellect1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/select")
sleep(1)
dizi=np.array(listofcurrencies).reshape(4,7)
print('You must choose from the list:\n',dizi,color="green")
input_currency_name=input('First currency name: ')
sellect1.send_keys(f'{input_currency_name}')
sleep(1)
sellect1.send_keys(Keys.ENTER)
sleep(1)

#second currency selection
sellect2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/select")
input_currency_name2=input('Second currency name: ')
sellect2.send_keys(f'{input_currency_name2}')
sleep(1)
sellect2.send_keys(Keys.ENTER)
sleep(1)

#return the result in the input box
try:
    input_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/input'))
    )
    value = input_element.get_attribute("value")
    print(f"Foreign currency: {input_value}:{input_currency_name.upper()} --> {value}:{input_currency_name2.upper()}",color='green')
except:
    print('Error',color='red')

sleep(5)
driver.quit()