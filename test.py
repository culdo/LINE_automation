import LINE

LINE.login("george0228489372@yahoo.com.tw", "wuorsut")

LINE.choose_room("TDK放天燈飛行組")

while True:
    text = LINE.has_new("Other")
    if text:
        LINE.send(text)
