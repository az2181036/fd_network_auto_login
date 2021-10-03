import json

import requests

url = "http://wlrz.fudan.edu.cn/include/auth_action.php"
headers = {"Connection": "keep-alive",
           "Host": "wlrz.fudan.edu.cn",
           "Content-Type": "application/x-www-form-urlencoded",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
data = {"action": "login",
        "username": "学号",
        "password": "密码",
        "ac_id": "1",
        "user_ip": "你的ip",
        "nas_ip": "",
        "user_mac": "",
        "save_me": "1",
        "ajax": 1}
res = requests.post(url=url, data=data, headers=headers, verify=False)
