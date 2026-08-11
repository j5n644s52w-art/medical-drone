import os
import requests

# 從 GitHub Secrets 讀取變數
CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
USER_ID = os.getenv('LINE_USER_ID')

def send_line_message():
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # 你的會議通知訊息
    message = """
【會議通知】
【醫療無人機中心 核心會議】
會議時間：每週二上午10:00
會議地點：五期B1急診會議室

    
    payload = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("發送成功！")
    else:
        print(f"發送失敗：{response.status_code}, {response.text}")

if __name__ == "__main__":
    send_line_message()
