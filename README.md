# LINE_automation
一個讓LINE操作自動化的工具
## 寫在前頭
* 首先有[Python環境](https://zh.wikipedia.org/wiki/Python#%E4%B8%93%E9%97%A8%E4%B8%BAPython%E8%AE%BE%E8%AE%A1%E7%9A%84IDE%E8%BD%AF%E4%BB%B6)
* 安裝瀏覽器自動化套件
```shell
pip install selenium
```
* 再來你只要下載`LINE.py`
## 使用
在你的Python腳本內Import
```python
import LINE

account = LINE("你的帳號", "沒忘的密碼", "手機信箱＠gmail.com")   # 登入賴，程式會自動發送驗證碼至手機信箱
account.set_room("110級機器人一甲")                            # 進賴群
account.send("我是一條訊息")                               # 發訊息
```
### 自動發送&回覆
```python
for i in range(10):
  account.send("自己傳十次訊息")  

while True:
  if account.has_new:
    account.send(account.read())  # 別人發什麼 你就回什麼
```

### 願望清單
- [x] ~~切換群組~~
- [x] ~~接收文字訊息~~
- [x] ~~接收圖片訊息~~
- [x] ~~改群組名稱~~
- [ ] 取得未讀群組清單
- [ ] 發圖片
- [ ] 發貼圖
