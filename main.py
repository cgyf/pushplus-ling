from crawler import fetch_notices
from push_handler import send_to_wechat,format_notices_message
from config import KEY_PASS
def crawler_wechat():
    try:
        resp = fetch_notices()
        message = format_notices_message(resp)
        result = send_to_wechat(KEY_PASS, "宿州学院通知栏", message)
        if result["code"] == 200:
            return "推送成功"
        else:
            return f"推送失败，{result['msg']}"
    except Exception as e:
        print(f"Error occurred: {e}")
if __name__ == "__main__":
    resp = crawler_wechat()
    print(resp)
