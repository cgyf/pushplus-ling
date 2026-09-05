from crawler import fetch_notices
from push_handler import send_to_wechat, format_notices_message
from config import KEY_PASS
from file_push import load_history, save_history
def crawler_wechat():
    try:
        notices = fetch_notices()
        if not notices:
            return "本次未抓取到公告，请检查网络或网页结构"
        history = load_history()
        new_items = [n for n in notices if n["url"] not in history]
        if not new_items:
            return "没有新公告，无需推送"
        message = format_notices_message(new_items)
        result = send_to_wechat(KEY_PASS, "宿州学院通知栏", message)
        if result.get("code") == 200:
            new_urls = [n["url"] for n in new_items]
            save_history(history + new_urls)
            return f" 成功推送 {len(new_items)} 条新公告"
        else:
            return f" 推送失败，{result.get('msg', '未知错误')}"
    except Exception as e:
        return f" 运行异常: {e}"
if __name__ == "__main__":
    result_msg = crawler_wechat()
    print(result_msg)
