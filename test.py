import LINE
import serial

LINE.login("george0228489372@yahoo.com.tw", "wuorsut", "wuorsut@gmail.com")
LINE.go_room("Alo Smo")

while True:
    last_cmd = LINE.has_new("Own")
    if last_cmd:
        print(last_cmd)

# print 'loop'
# if ser.in_waiting > 0:
#     ser.reset_input_buffer()
#     read_ser = ser.readline()
#     print read_ser
#     send_msg(read_ser)