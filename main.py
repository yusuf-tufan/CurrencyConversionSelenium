from tkinter import messagebox
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import numpy as np
from tkinter import *
import time

#time
local_time = time.localtime()

window=Tk()
window.title('Currency Converter')
window.config(bg='silver')
window.state('zoomed')

listofcurrencies=['TRY','USD','EUR','CHF','GBP','CAD','AUD','CNY','RUB','CNH','SEK',
                  'KWD','PKR','QAR','DKK','SAR','BGN','RON','NOK','IRR',
                  'JPY','ZAR','RSD','AED','BYN','TJS','','']

def result():
    global listofcurrencies,local_time
    try:
        user_amount = float(enter_amount.get())
        user_currency = str(enter_first.get())
        user_currency2 = str(enter_second.get())

        if user_amount==0:
            messagebox.showinfo(message='You cannot enter 0 amount',title='Error')
        elif len(user_currency)!=3 :
            messagebox.showinfo(message='Enter Currency Name Correctly', title='Error')
        elif len(user_currency2)!=3 :
            messagebox.showinfo(message='Enter Currency Name Correctly', title='Error')
        else:
            #button disabled
            btn_start.config(state="disabled")

            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome()
            driver.minimize_window()

            # Go to URL
            url = 'https://www.foreks.com/doviz/'
            driver.get(url)
            sleep(1)
            driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

            #money amount entry and sending
            value1=driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/input")
            value1.clear()
            value1.send_keys(f'{user_amount}')

            #currency selection
            sellect1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/select")
            sellect1.send_keys(f'{user_currency}')
            sellect1.send_keys(Keys.ENTER)

            #second currency selection
            sellect2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/select")
            sellect2.send_keys(f'{user_currency2}')
            sellect2.send_keys(Keys.ENTER)

            #return the result in the input box
            try:
                input_element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/input'))
                )
                value = input_element.get_attribute("value")
                time_str = time.strftime("%m/%d/%Y\n%H:%M:%S")
                lbl_result.config(text=f"Exchange Rate: {user_amount}:{user_currency.upper()} --> {value}:{user_currency2.upper()}\n"
                                       f"Time: {time_str}",
                                  bg='black',fg='light green',font=('Arial',15,'bold'))

            except:
                lbl_error=Label(text='Error')
                lbl_error.pack()

            driver.quit()
    except:
        messagebox.showinfo(message='Enter Correct Data', title='Error')

def clear_all():
    lbl_result.config(text='',bg='silver')
    enter_amount.delete(0,END)
    enter_first.delete(0,END)
    enter_second.delete(0,END)

    # button active
    btn_start.config(state='active',bg='light green')

#list of currencies
dizi=np.array(listofcurrencies).reshape(4,7)
lbl_list=Label(text=f'Enter the first amount -> currency name1 -> currency name2 -> Currency Conversion\n\n'
                    f'You must select your currency from the list:\n\n'
                    f'{dizi}',bg='brown',fg='white',font=('Arial',12,'bold'))
lbl_list.pack(pady=(0,20))

#Enter amount
lbl_enter=Label(text='Enter amount',font=('Arial',10,'bold'))
lbl_enter.pack(pady=(0,5))
enter_amount=Entry(width=15)
enter_amount.pack(pady=(0,10))

#Enter currency names
lbl_enter_first=Label(text='Enter currency names',font=('Arial',10,'bold'))
lbl_enter_first.pack(pady=(0,2))
enter_first=Entry(width=10)
enter_first.pack(pady=(0,1))

lbl_enter_second=Label(text='TO',font=('Arial',10,'bold'))
lbl_enter_second.pack(pady=(0,2))

enter_second=Entry(width=10)
enter_second.pack(pady=(0,20))

#start button
lbl_start=Label(text='You Must Start To The URL\nWait After Pressing...',font=('Arial',9,'bold'))
lbl_start.pack(padx=200,pady=5)
btn_start=Button(text='Convert Currency',bg='light green',command=result )
btn_start.pack(pady=(0,10))

#result label
lbl_result=Label(text='',bg='silver',fg='light green',font=('Arial',15,'bold'))
lbl_result.pack(pady=(0,10))

#clear the window
btn_clear=Button(text='CLAER ALL',fg='white',bg='red',font=('Arial',9,'bold'),command=clear_all)
btn_clear.pack(pady=(0,10))


window.mainloop()