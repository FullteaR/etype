import time
from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import re
import pyautogui
import selenium

pattern=re.compile('<span>(.*)</span></div>$')
print(pattern)

driver = webdriver.Chrome()
driver.get('https://www.e-typing.ne.jp/app/jsa_std/typing.asp?t=trysc.trysc.trysc.std.0&u=&s=0')
start = driver.find_element_by_id("start_btn")
start.click()
#pyautogui.press(" ")
time.sleep(3)
word_old=""
while True:
    try:
        element=driver.find_element_by_id("sentenceText")
    except selenium.common.exceptions.NoSuchElementException:
        continue
    word=element.get_attribute("innerHTML")
    search=pattern.search(word)
    if search is None:
        continue
    word=search.group(1)

    print(word)
    if word_old==word:
        continue
    word=word.replace("SI","SHI")
    spr1=len(word)//4
    spr2=spr1*2
    spr3=spr1*3
    pyautogui.typewrite(word[:spr1])
    pyautogui.typewrite(word[spr1:spr2])
    pyautogui.typewrite(word[spr2:spr3])
    pyautogui.typewrite(word[spr3:])
    word_old=word
time.sleep(10)
driver.quit()
