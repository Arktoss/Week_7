from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from pynput. keyboard import Key, Controller
import mouse
from pynput.mouse import In, Out

web = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # opens google.
web.get('https://docs.google.com/forms/d/e/1FAIpQLScXNbdAs0HF9d5DHFXo1qTjK9wMSrG1nBCb1lzFw0tkJUGvOw/viewform')

time.sleep(500)

mouse.wheel(-1)

mouse.click('left')
In [22]: mouse.get_position()
Out[22]: (100, 100)

keyboard = Controller()
key1 = "Ctrl"
key2 = "V"
keyboard. press(key1)
keyboard. release(key2)