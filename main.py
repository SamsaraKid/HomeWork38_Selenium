from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# def request(req, data):



while True:
    prompt = int(input('Что хотите найти:\n'
                   '\t1 - Погода\n'
                   '\t2 - Картинки котов\n'
                   '\t3 - Карта города\n'))
    if prompt == 1:
        driver = webdriver.Chrome()
        driver.get('https://ya.ru/')
        elem1 = driver.find_element(By.XPATH, '//*[@id="text"]')
        elem1.send_keys('Погода')
        time.sleep(1)
        elem2 = driver.find_elements(By.CLASS_NAME, 'mini-suggest__popup-content')
        elem2[0].click()
        # suggest-item-8as3z1ica88-0 > a:nth-child(1)


    elif prompt == 2:
        prompt = 'Картинки котов'
    elif prompt == 3:
        prompt = 'Карта города'




# time.sleep(2)
# elem2 = driver.find_element(By.XPATH, '/html/body/main/div[2]/form/div[2]/button')
# elem2.click()


# time.sleep(3)
# driver.close()


