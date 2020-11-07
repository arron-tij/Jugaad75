import time
from selenium import webdriver
import datetime
import webbrowser
from subprocess import Popen
import os    
while True:
    x = datetime.datetime.today()
    if x.weekday() == 5 or x.weekday() == 6:
        print("Hell")
        time.sleep(10)
        pass
    else:
        # dr = webdriver.Chrome()
        # dr.get('http://localhost:8000/')
        # time.sleep(3)
        # dr.quit()
        webbrowser.open('http://localhost:8000/')
        time.sleep(10)
        os.system("taskkill /im chrome.exe /f")
        time.sleep(10)