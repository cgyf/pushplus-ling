import requests
from config import KEY_PASS
import json
def send_to_wechat(token,title,content):
    url = "https://www.pushplus.plus/send"
    payload = json.dumps({
        "token": token,
        "title": title,
        "content": content
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        if response.status_code != 200:
            return {"code":-1,"msg":f"请求失败,状态码为{response.status_code}"}
        result_json=response.json()
        return result_json
    except Exception as e:
        return {"code": -999, "msg": f"网络连接异常: {e}"}
def format_notices_message(notices):
    if not notices:
        return "暂时无新通告"
    messages = "通知公告如下\n"
    for idx, item in enumerate(notices, 1):
        messages += f"{idx}. {item['title']} | {item['times']} | <a href={item['url']}>点击查看详情</a>\n"
    return messages
if __name__ == "__main__":
    from crawler import fetch_notices
    print(format_notices_message(fetch_notices()))