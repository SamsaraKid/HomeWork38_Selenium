from selenium import webdriver
from selenium.webdriver.common.by import By
import time

while True:
    req = int(input('Что хотите найти:\n'
                   '\t1 - Погода\n'
                   '\t2 - Картинки котов\n'
                   '\t3 - Карта города\n'))
    if req == 1:
        driver = webdriver.Firefox()
        driver.get('https://ya.ru/')
        elem1 = driver.find_element(By.XPATH, '//*[@id="text"]')
        elem1.send_keys('Погода')
        time.sleep(1)
        elem2 = driver.find_elements(By.CLASS_NAME, 'mini-suggest__popup-content')
        elem2[0].click()
        try:
            elem3 = driver.find_element(By.CLASS_NAME, 'DistrSplashscreen-DeclineButton')
            elem3.click()
        except:
            pass
        time.sleep(5)
        driver.close()
    elif req == 2:
        driver = webdriver.Firefox()
        driver.get('https://yandex.ru/images/')
        elem1 = driver.find_element(By.NAME, 'text')
        elem1.send_keys('Коты')
        time.sleep(1)
        elem2 = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/div[1]/form/div[2]/button/div[3]')
        elem2.click()
        time.sleep(5)
        driver.close()
    elif req == 3:
        city = input('Введите город:\n')
        driver = webdriver.Firefox()
        driver.get('https://yandex.ru/maps/')
        elem1 = driver.find_element(By.CLASS_NAME, 'input__control')
        elem1.send_keys(city)
        time.sleep(1)
        elem2 = driver.find_element(By.CLASS_NAME, 'small-search-form-view__button')
        elem2.click()
        time.sleep(5)
        driver.close()
    else:
        break








