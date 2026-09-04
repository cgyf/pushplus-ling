from crawler import fetch_notices
from push_handler import send_to_wechat,format_notices_message
from config import KEY_PASS
def crawler_wechat():
    try:
        resp = fetch_notices()
        message = format_notices_message(resp)
        result = send_to_wechat(KEY_PASS, "宿州学院通知栏", message)
        if result["code"] == 200:
            return {"code": 0, "msg": "ok"}
        else:
            return {"code": -1, "msg": result["msg"]}
    except Exception as e:
        print(f"Error occurred: {e}")
if __name__ == "__main__":
    resp = crawler_wechat()
    if resp["code"] == 0:
        print("推送成功")
    else:
        print(resp["msg"])