## chatGPT聊天机器人demo
本项目用最少的代码接入了chatGPT的接口，实现了类似于聊天机器人的功能，你可以基于你的需求在此基础上改动

### 技术架构
Flask + gunicorn + jquery

### 环境要求
python3

备注：
如果是本地调试，需要有🪜；
如果是部署到服务器，需要是海外服务器

### 准备
1. `pip install -r requirements.txt`
2. 替换`main.py`中的api key为你自己的api key，申请方式：https://platform.openai.com/account/api-keys
3. 如果是部署到服务器上，还需要修改pages/chat.html中ajax访问的后端地址url为真实服务器的ip或域名

### 运行
`bash start.sh`

### 体验效果
在浏览器打开 `ip:5000/chat` 即可， 注意替换ip为你的服务器ip，本地调试的话直接输入 `127.0.0.1:5000/chat`