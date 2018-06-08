from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import serial
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

gmail_user = 'cbc106008@stmail.nptu.edu.tw'
gmail_passwd = 'f130464947'

sent_from = gmail_user
TO = "wuorsut@gmail.com"
SUBJECT = "LINE自動請求"
TEXT = "賴驗證碼："

msg = MIMEMultipart('alternative')

msg['Subject'] = SUBJECT
msg['From'] = sent_from
msg['To'] = TO

# ser=serial.Serial("/dev/ttyUSB0",115200)
p="/dev/ttyUSB0"
while True:
    error_flag = False
    try:
        ser = serial.Serial(p, 115200)
    except Exception as e:
        error_flag = True
        if "ttyUSB0" in str(e):
            p = "/dev/ttyUSB1"
            print ("port is now", p)
        elif "ttyUSB1" in str(e):
            p = "/dev/ttyUSB0"
            print ("port is now", p)
        else:
            print (e)   # none of the above

    if not error_flag:
        break

    time.sleep(1)

jquery = r'$("#_chat_room_input").text(arguments[0])'


def send_msg(msg):
    #browser.find_element_by_id("_chat_room_input").send_keys(msg)
    browser.execute_script(jquery, msg)
    input_area.send_keys(Keys.ENTER)


chrome_option = Options()
chrome_option.add_argument("--load-extension=/home/lab-pc1/PycharmProjects/Line_Auto/2.1.4_0/")
#chrome_option.add_argument('--headless')

browser = Chrome(chrome_options=chrome_option)
browser.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html"
)
element = WebDriverWait(browser, 99).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#line_login_email")))

browser.find_element_by_id("line_login_email").send_keys("george0228489372@yahoo.com.tw")
browser.find_element_by_id("line_login_pwd").send_keys("wuorsut")
browser.find_element_by_id("login_btn").send_keys(Keys.ENTER)

# sent LINE validation code to smartphone
msg.attach(MIMEText(TEXT, 'plain'))
server = smtplib.SMTP('stmail.nptu.edu.tw')
server.ehlo()
server.login(gmail_user, gmail_passwd)
server.sendmail(gmail_user, TO, msg.as_string())
print ('email sent')
server.quit()

element = WebDriverWait(browser, 99).until(
        EC.presence_of_element_located((By.XPATH, '//*[@data-chatid="c487f9de47e6548464b2de60dd4c85cc2"]')))
time.sleep(1)

element.click()

input_area = browser.find_element_by_id("_chat_room_input")
time.sleep(0.5)
data_local_id = browser.find_element_by_css_selector("div.mdRGT07Own:last-child").get_attribute("data-local-id")

while True:
    data_local_id_now = browser.find_elements_by_css_selector("div.mdRGT07Own")[-1].get_attribute("data-local-id")
    if data_local_id != data_local_id_now:
        last_cmd = browser.find_elements_by_css_selector("div.mdRGT07Own .mdRGT07MsgTextInner")[-1].text
        print(last_cmd)
        if last_cmd == u"往前":
            ser.write("1".encode())
            print(1)
        elif last_cmd == u"往後":
            ser.write("2".encode())
            print(2)
        elif last_cmd == u"往左":
            ser.write("3".encode())
            print(3)
        elif last_cmd == u"往右":
            ser.write("4".encode())
            print(4)
        elif last_cmd == u"停車":
            ser.write("5".encode())
            print(5)
        data_local_id = data_local_id_now
    # print 'loop'
    # if ser.in_waiting > 0:
    #     ser.reset_input_buffer()
    #     read_ser = ser.readline()
    #     print read_ser
    #     send_msg(read_ser)
