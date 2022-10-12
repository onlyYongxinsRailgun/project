import requests
# pip install pwinput
import pwinput

# 繼承
def sendLine(message):
    # HTTP 標頭參數與資料
    headers = { "Authorization": "Bearer " + token }
    data = { 'message': message }

    # 以 requests 發送 POST 請求
    requests.post("https://notify-api.line.me/api/notify",
    headers = headers, data = data)

class medicine:
    def __init__(self, msgType):
        self.msgType = msgType

    # 取得用藥警告類型
    def get_msgType(self):
        return self.msgType

    # 更改用藥警告類型 
    def set_msgType(self, msgType):
        self.msgType = msgType

    # 發出用藥異常警告
    def warning(self):
        self.msg = "用藥異常！" + str(self.get_msgType())
        print(self.msg)
        sendLine(self.msg)

class heart:
    def __init__(self, msgType):
        self.msgType = msgType
        self.size = 10
        self.list = []
    # 取得心律警告類型
    def get_msgType(self):
        return self.msgType

    # 更改心律警告類型 
    def set_msgType(self, msgType):
        self.msgType = msgType

    # 發出心律異常警告
    def warning(self):
        print("心律異常！")
        # sendLine("心律異常！")
    
    # 連續資料queue結構
    def add_in_queue(self, data):
        if(len(self.list) < self.size):
            self.list.append(data)
            return True
        return False

# 前置
# LINE Notify 權杖
token = pwinput.pwinput(prompt='輸入權杖：', mask='*')

print("連結成功！")
# sendLine("連結成功！")

# medicineNotify = ["沒吃藥", "吃藥丸A"]

m = medicine("沒吃藥")
m.warning()
m1 = medicine("吃藥丸A")
m1.warning()