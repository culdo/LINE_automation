from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os, time, platform
from selenium.common.exceptions import WebDriverException
stu_user = 'use4rline@gmail.com'
stu_passwd = 'CIR4LINE'
TEXT = "驗證碼："
mail = MIMEMultipart('alternative')
mail['From'] = stu_user
mail['Subject'] = "LINE自動請求"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(stu_user, stu_passwd)

jquery = r'$("#_chat_room_input").text(arguments[0])'
chrome_option = Options()
# chrome_option.add_argument('--headless')
if platform.system() == 'Linux':
    chrome_option.add_argument("--load-extension=" + os.environ['HOME'] + "/.config/google-chrome/Profile 1/Extensions/ophjlpahpchlmihnnnihgmmeilfjmjjc/2.1.4_0/")
else:
    chrome_option.add_argument("--load-extension=" + os.environ[
        'userprofile'] + r"\AppData\Local\Google\Chrome\User Data\Default\ophjlpahpchlmihnnnihgmmeilfjmjjc\2.1.4_0")
browser = Chrome(chrome_options=chrome_option)


def go_room(room):
    global data_local_id, input_area

    element = WebDriverWait(browser, 99).until(
        EC.presence_of_element_located((By.XPATH, '//*[@title="'+room+'"]')))
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

    time.sleep(0.5)
    data_local_id = browser.find_element_by_css_selector("div.MdRGT07Cont:last-child").get_attribute("data-local-id")
    input_area = browser.find_element_by_id("_chat_room_input")


def has_new(setwho="Other"):
    global data_local_id
    if setwho == "ALL":
        updated = browser.find_elements_by_class_name("MdRGT07Other")[-1]
    else:
        updated = browser.find_elements_by_class_name("mdRGT07"+setwho)[-1]
    data_local_id_now = updated.get_attribute("data-local-id")
    if data_local_id != data_local_id_now:
        data_local_id = data_local_id_now
        new_text = 0
        while not new_text:
            new_text = updated.find_element_by_class_name("mdRGT07MsgTextInner").text
        return new_text



def read():
    return browser.find_elements_by_css_selector("div.mdRGT07Own .mdRGT07MsgTextInner")[-1].text


def send(msg):
    # data_local_id = browser.find_elements_by_css_selector("div.mdRGT07Cont").get_attribute("data-local-id")
    browser.execute_script(jquery, msg)
    try:
        input_area.send_keys(Keys.ENTER)
    except WebDriverException:
        input_area.click()
        input_area.send_keys(Keys.ENTER)


def login(username, pwd, email=None):
    if email is None:
        email = username
    browser.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html"
    )
    element = WebDriverWait(browser, 99).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#line_login_email")))

    element.send_keys(username+Keys.TAB+pwd+Keys.ENTER)
    # browser.find_element_by_id("line_login_pwd").send_keys("wuorsut")
    # browser.find_element_by_id("login_btn").send_keys(Keys.ENTER)
    element = WebDriverWait(browser, 99).until(
            EC.presence_of_element_located((By.CLASS_NAME, "mdCMN01Code")))

    # sent LINE validation code to smartphone
    # mail['Subject'] = SUBJECT+element.text
    mail['To'] = email
    mail.attach(MIMEText(TEXT+element.text, 'plain'))
    server.sendmail(stu_user, mail['To'], mail.as_string())
    print('email sent')
    server.quit()

