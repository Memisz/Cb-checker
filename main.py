from requests_toolbelt.threaded import pool
import requests
import queue
import json

from styler import Color

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from config import read_config

import time
import random
import string

a_file = open("emaillist.txt", "r")

list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)

a_file.close()

print(list_of_lists)


def emailchecker(email1):
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument('--window-size=1920,1080')
    # options.add_argument('--proxy-server="direct://"')
    # options.add_argument('--proxy-bypass-list=*')
    driver = webdriver.Chrome(r"chromedriver.exe", options=options)
    driver.get("https://www.coinbase.com/signup")
    driver.maximize_window()
    fname = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/form/div[1]/div[1]/input')
    fname.send_keys('John')

    lname = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/form/div[1]/div[2]/input')
    lname.send_keys('Doe')

    email = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/form/div[2]/input')
    email.send_keys(email1)

    password = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/form/div[3]/div/div[1]/input')
    password.send_keys('abdsAKDJW1029-_.!')

    tos = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/form/div[5]/div').click()

    submit = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/form/button').click()
    time.sleep(3)
    try:
        b = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/form/div[6]/div')
        if b.text == 'An account already exists with this email address.':
            print(Color.green + f'[REGISTERED] {email1}')
        else:
            print(Color.red + f'[ERROR] {email1}')
        driver.quit()
        with open('registered.txt', 'a') as filereg:
            filereg.write(f"{email1}\n")
        return True
    except:
        print(Fore.RED + f'[UNREGISTERED] {email1}')
        driver.quit()
        with open('unregistered.txt', 'a') as fileunreg:
            fileunreg.write(f"{email1}\n")
        return False


for x in list_of_lists:
    emailchecker(x[0])
    time.sleep(15)
