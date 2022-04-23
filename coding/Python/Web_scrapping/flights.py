
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re


kayak_dict = {'url': 'https://www.kayak.com/flights/',
                'From':'//*[@id="c3YaY"]/div[13]/div/div[2]/div[1]/div[2]/div/input',
                'To':'//*[@id="c3YaY"]/div[13]/div/div[2]/div[1]/div[2]/div/input',
                'search_btn':'//*[@id="ESZS"]/div/div/div/div[1]/div[2]/div/div[5]/button/div[1]/div/svg/path'
}

b = webdriver.Chrome(ChromeDriverManager().install())
b.get(kayak_dict['url'])
b.implicitly_wait(5)
b.find_element(by=By.XPATH,value=kayak_dict['From']).send_keys('London')
b.find_element(by=By.XPATH,value=kayak_dict['To']).send_keys('Rome')
b.find_element(by=By.XPATH,value=kayak_dict['search_btn']).click()


sky_dict = {'url': 'https://www.skyscanner.net/flights/',
                'cokies':'//*[@id="acceptCookieButton"]',    
                'From':'//*[@id="fsc-origin-search"]',
                'To':'//*[@id="fsc-destination-search"]]',
                'search_btn':'//*[@id="flights-search-controls-root"]/div/div/form/div[3]/button'

}

b =  webdriver.Chrome(ChromeDriverManager().install())
b.get(sky_dict['url'])
b.find_element(by=By.XPATH,value=sky_dict['cokies']).click()
b.implicitly_wait(5)
b.find_element(by=By.XPATH,value=sky_dict['From']).send_keys('London')
b.find_element(by=By.XPATH,value=sky_dict['To']).send_keys('Rome')
b.find_element(by=By.XPATH,value=sky_dict['search_btn']).click()
