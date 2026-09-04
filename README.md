
pushplus‑ling/
├── config.py          # 配置密钥（PushPlus token）
├── crawler.py         # 网页爬虫，抓取通知
├── push_handler.py    # 推送底层逻辑，网络请求全部放这里
├── main.py            # 主调度：抓取、去重、调用推送
├── sent.json          # 自动生成，记录已经推送过通知 id
└── run.log            # 自动生成，运行日志
