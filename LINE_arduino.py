from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import serial

def send_msg(msg):
    browser.find_element_by_id("chat_room_input_scroll").click()
    browser.find_element_by_id("_chat_room_input").send_keys(msg)
    browser.find_element_by_id("_chat_room_input").send_keys(Keys.ENTER)


chrome_option = Options()
chrome_option.add_argument("load-extension=./2.1.4_0/")

browser = Chrome(chrome_options=chrome_option)
browser.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html"
)
time.sleep(0.1)
browser.find_element_by_id("line_login_email").send_keys("george0228489372@yahoo.com.tw")
browser.find_element_by_id("line_login_pwd").send_keys("wuorsut")
browser.find_element_by_id("login_btn").send_keys(Keys.ENTER)

element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h1.mdRGT04Ttl")))

send_msg("eeee")
send_msg("fffff")
