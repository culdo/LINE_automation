from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyUSB0",115200) 

def send_msg(msg):
    #browser.find_element_by_id("_chat_room_input").send_keys(msg)
    browser.execute_script(r'$("#_chat_room_input").text(arguments[0])', msg)
    browser.find_element_by_id("_chat_room_input").send_keys(Keys.ENTER)


chrome_option = Options()
chrome_option.add_argument("--load-extension=./2.1.4_0/")
#chrome_option.add_argument('--headless')

browser = Chrome(chrome_options=chrome_option)
browser.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html"
)
element = WebDriverWait(browser, 99).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#line_login_email")))

browser.find_element_by_id("line_login_email").send_keys("george0228489372@yahoo.com.tw")
browser.find_element_by_id("line_login_pwd").send_keys("wuorsut")
browser.find_element_by_id("login_btn").send_keys(Keys.ENTER)

element = WebDriverWait(browser, 99).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="_chat_list_body"]/li[1]/div')))
browser.find_element_by_xpath('//*[@id="_chat_list_body"]/li[1]/div').click()
time.sleep(1)

browser.find_element_by_id("chat_room_input_scroll").click()
while True:
    read_ser=ser.readline()
    send_msg(read_ser)