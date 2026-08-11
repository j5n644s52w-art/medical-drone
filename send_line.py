import os
import requests

# ==========================================
# 🛑 請在這裡貼上你的專屬金鑰與 ID 
# (務必保留前後的雙引號 "")
# ==========================================

CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
USER_ID = os.getenv('LINE_USER_ID')

# ==========================================

def send_line_message():
    url = "https://api.line.me/v2/bot/message/push"
    
    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # 這裡的三個引號 """ 已經幫你完美對齊與封口
    message = """【會議通知】
【醫療無人機中心 核心會議】
會議時間：每週二上午10:00
會議地點：五期B1急診會議室
出席成員：王曉明"""
    
    payload = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    
    print("⏳ 開始傳送訊息給 LINE 伺服器...")
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("🎉 發送成功！趕快去檢查你的 LINE 群組有沒有收到無人機中心會議通知！")
        else:
            print(f"❌ 發送失敗：狀態碼 {response.status_code}")
            print(f"🔍 LINE 官方退件理由：{response.text}")
            
    except Exception as e:
        print(f"❌ 程式執行發生嚴重錯誤：{e}")

if __name__ == "__main__":
    send_line_message()
