from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import random
import configparser
import os
import sys

#configファイル読み込み.
dpath = os.path.dirname(sys.argv[0])
config = configparser.ConfigParser()
path = dpath + '/config.ini'
config.read(path, 'UTF-8')

url = config['data']['url']#url
num = config['data']['num']
profpass = config['chrome']['profilepass']#profilepass

tem = str(36 + random.randint(3, 8) / 10) #ランダム体温

#UserProfileSetting
ChromeDriverManager().install()
options = webdriver.ChromeOptions()
userDir = profpass
options.add_argument('--user-data-dir=' + userDir)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options)


#現在時刻取得.
dt_now = datetime.datetime.now()
now = dt_now.time()
#比較時刻.
gozen = datetime.time(6, 0, 0)
gogo = datetime.time(12, 10, 0)
gekou = datetime.time(14, 50, 0)

driver.get(url)

STnum =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
STnum.send_keys(num)

if(gozen <= now <gogo):#午前登録.
    radio_buttons =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    radio_buttons.click()
elif(gogo <= now <gekou):#午後登録.
    radio_buttons =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span')
    radio_buttons.click()
elif(gekou <= now):#下校登録.
    radio_buttons =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span')
    radio_buttons.click()

#次へ.
next_buttons =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
next_buttons.click()

if(gozen <= now <gekou):#体温記録.
    wait = WebDriverWait(driver, 10) #読み込み待ち.
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')))

    tem_buttons =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    tem_buttons.click()

    next_buttons =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span')
    next_buttons.click()

    wait = WebDriverWait(driver, 10) #読み込み待ち.
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]/span')))

    tem_textbox =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input') #ランダム体温を入力
    tem_textbox.send_keys(tem)

    send_buttons =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]/span')
    send_buttons.click()

elif(gekou <= now):#下校登録.
    wait = WebDriverWait(driver, 10) #読み込み待ち.
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]/span')))

    send_buttons =driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]/span')
    send_buttons.click()

driver.quit()