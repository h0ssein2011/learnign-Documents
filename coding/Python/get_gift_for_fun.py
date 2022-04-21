from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


count = 0
my_gift  = 0
while my_gift != 7:
    try:
        b = webdriver.Chrome(ChromeDriverManager().install())
        url = 'https://bigbox.ee/'
        b.get(url)
        # click the gift button
        btn = b.find_element(by=By.CLASS_NAME,value='soundest-form-wof-open')
        btn.click()
        print('button clicked')
        
        # wait for the form to load
        time.sleep(3)

        # fill the input field with name
        form = b.find_elements(by=By.CLASS_NAME,value='soundest-form-wof-field')
        name = form[0]
        name.send_keys('hd11sshjdsre'+str(random.randint(1,100)))
        print('name filled')

        # fill the input field with email
        email = form[1]
        email.send_keys(f'hdfggf{random.randint(1,100)}@yahoo.com')
        print('email filled')
        
        # fill terms 
        terms = b.find_element(by=By.CLASS_NAME,value='soundest-form-wof-checkbox-checkmark')
        terms.click()
        print('terms checked')

        #click submit button
        submit = b.find_element(by=By.CLASS_NAME,value='soundest-form-wof-submit')
        submit.click()
        print('submit sent')

        # wait for the form to load 
        time.sleep(50)
        gift = b.find_element(by=By.CLASS_NAME,value='soundest-form-wof-coupon-code')
        print(gift.get_attribute("textContent"))
        my_gift = int(gift.get_attribute("textContent")[0])
        if my_gift == 7:
            print(gift.get_attribute("textContent"))
     
        b.close()

    except Exception as e:
        print(e)
    count +=1
    print('iteration done: ', count)