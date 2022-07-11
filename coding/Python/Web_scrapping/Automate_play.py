
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
import time
import re

url = 'https://static-demo.contentmedia.eu/ecf2/index.html?gameid=10079&operatorid=7770110&currency=EUR&mode=real&device=desktop&token=Hosin%40Olybet&gamename=tacobrothersderailed&language=en_gb&lobbyurl=https%3A%2F%2Fpine.elk-studios.com&extension=screenname%3AHosin%40Olybet&capi=https%3A%2F%2Fgc1-demo.contentmedia.eu%2Fcapi&papi=https%3A%2F%2Fpapi-demo.contentmedia.eu'

X_paths = {'sound':'/html/body/div[3]/canvas',
'train':'/html/body',
'Ok_btn':'ui-canvas',
}


b = webdriver.Chrome(ChromeDriverManager().install())
b.get(url)
time.sleep(10)
print('Ready to click sound button')
b.find_element(by=By.XPATH,value=X_paths['sound']).click()
time.sleep(10)
print('Ready to click train button')
b.find_element(by=By.XPATH,value=X_paths['train']).click()
time.sleep(10)
print('Ready to click Ok button')
canvas = b.find_element(by=By.ID,value=X_paths['Ok_btn'])
#https://www.youtube.com/watch?v=NebFQ31NFtE
width = canvas.get_attribute('style').split('width:')[1].split('px;')[0]
height = canvas.get_attribute('style').split('height:')[1].split('px;')[0]
print(height,width)

drawing = ActionChains(b).move_by_offset(-100, -105).click(on_element=canvas)
# drawing.perform()

