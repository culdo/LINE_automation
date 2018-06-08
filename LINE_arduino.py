from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os, time
from selenium.common.exceptions import WebDriverException
stu_user = 'use4rline@gmail.com'
stu_passwd = 'CIR4LINE'
sent_from = stu_user
TO = "wuorsut@gmail.com"
TEXT = "驗證碼："
msg = MIMEMultipart('alternative')
msg['From'] = sent_from
msg['To'] = TO
msg['Subject'] = "LINE自動請求"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(stu_user, stu_passwd)

jquery = r'$("#_chat_room_input").text(arguments[0])'


def send_msg(msg):
    #browser.find_element_by_id("_chat_room_input").send_keys(msg)
    browser.execute_script(jquery, msg)
    try:
        input_area.send_keys(Keys.ENTER)
    except WebDriverException:
        input_area.click()
        input_area.send_keys(Keys.ENTER)


chrome_option = Options()
chrome_option.add_argument("--load-extension="+os.environ['HOME']+"/.config/google-chrome/Profile 1/Extensions/ophjlpahpchlmihnnnihgmmeilfjmjjc/2.1.4_0/")
#chrome_option.add_argument('--headless')

browser = Chrome(chrome_options=chrome_option)
browser.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html"
)
element = WebDriverWait(browser, 99).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#line_login_email")))

element.send_keys("george0228489372@yahoo.com.tw"+Keys.TAB+"wuorsut"+Keys.ENTER)
# browser.find_element_by_id("line_login_pwd").send_keys("wuorsut")
# browser.find_element_by_id("login_btn").send_keys(Keys.ENTER)
element = WebDriverWait(browser, 99).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mdCMN01Code")))

# sent LINE validation code to smartphone
# msg['Subject'] = SUBJECT+element.text
msg.attach(MIMEText(TEXT+element.text, 'plain'))
server.sendmail(stu_user, TO, msg.as_string())
print('email sent')
server.quit()

element = WebDriverWait(browser, 99).until(
        EC.presence_of_element_located((By.XPATH, '//li[@title="沒有彤彤哥的D301"]')))
element.click()

data_local_id = WebDriverWait(browser, 99).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.MdRGT07Cont:last-child"))).get_attribute("data-local-id")
# data_local_id = browser.find_elements_by_css_selector("div.mdRGT07Cont").get_attribute("data-local-id")
input_area = browser.find_element_by_id("_chat_room_input")
