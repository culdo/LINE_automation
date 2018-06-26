# LINE_automation
一個讓LINE操作自動化的工具
## 寫在前頭
1. 首先有[Python3環境](https://zh.wikipedia.org/wiki/Python#%E4%B8%93%E9%97%A8%E4%B8%BAPython%E8%AE%BE%E8%AE%A1%E7%9A%84IDE%E8%BD%AF%E4%BB%B6)
2. 下載chromedriver：[Windows](https://chromedriver.storage.googleapis.com/2.40/chromedriver_win32.zip)、[Linux](https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip) \
解壓後把exe丟進`C:\Windows`目錄下
3. 安裝瀏覽器自動化套件
```shell
pip3 install selenium
```
* 再來你只要下載[LINE.py](https://culdo.github.io/LINE_automation/LINE.py)
## 使用
在你的Python腳本內Import
```python
import LINE

LINE.login("你的帳號", "沒忘的密碼", "用LINE的手機信箱＠gmail.com")   # 登入賴，程式自動發送登入驗證碼至手機信箱

LINE.choose_room("110級機器人一甲")                            # 進賴群
LINE.send("我是一條訊息")                                  # 發訊息

```
#### 自動發送&回覆
```python
for i in range(10):
  LINE.send("自己傳十次訊息")  

while True:
  msg = LINE.has_new("Other")                          # 別人發什麼
  if msg:
    LINE.send(msg)                                     # 你就回什麼
```

### 願望清單
- [x] ~~切換群組~~
- [x] ~~接收文字訊息~~
- [x] ~~接收圖片訊息~~
- [x] ~~改群組名稱~~
- [ ] 取得未讀群組清單
- [ ] 發圖片
- [ ] 發貼圖

# License
MIT
