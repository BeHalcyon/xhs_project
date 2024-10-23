import json
import os

import execjs
import requests

def transferCookies(cookies):
    cookiesList = cookies.split(';')
    cookiesJs = []
    for value in cookiesList:
        if value == "":
            continue
        cookiesJs.append(value)
    return cookiesJs

url = "https://edith.xiaohongshu.com/api/sns/web/v1/comment/post"

payload = "{\"note_id\":\"66f3dc30000000001a022758\",\"content\":\"+1\",\"target_comment_id\":\"66f49acc000000002400a70f\",\"at_users\":[]}"
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://www.xiaohongshu.com',
    'priority': 'u=1, i',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8'
}

cookie = "xsecappid=xhs-pc-web; a1=18dfad38995dqrlj5gm1jba0u2ve1oe9drlpvae6150000392391; webId=33726a7a9a13de412bb7ce4d261fefa0; gid=yYfi0fqYDYfDyYfi0fqYjF0dj2fAF1V2k6yV1KyD087JhU28dyldjh888qjJqjy8fYjjdjy2; abRequestId=33726a7a9a13de412bb7ce4d261fefa0; webBuild=4.39.0; websectiga=cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c; sec_poison_id=4ed1077d-29bf-41c9-8366-f969515c4b61; acw_tc=0cf569802356201734afe4140df53b1c6596ec639782cbc72c7e015b22a0670a; web_session=0400698ed6dc9256561e5a8522354b06ac97bd; unread={%22ub%22:%226704f702000000002a0331c9%22%2C%22ue%22:%2266fa8f20000000002c01661c%22%2C%22uc%22:28}"  # put your cookie here
payload = {
        "note_id": "66f3dc30000000001a022758",
        "content": "+1",
        "target_comment_id": "66f49acc000000002400a70f",
        "at_users": []
    }
api = url[url.find("/api"):]


def parsResult(e, cookies, t=None):
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "xhs_decrypt.js")
    return execjs.compile(open(file_path, 'r', encoding='utf-8').read()).call('XsXt', e, t, transferCookies(cookies))

xs_xt = parsResult(api, cookie, payload)

headers['cookie'] = cookie
headers['X-s'] = xs_xt['X-s']
headers['X-t'] = str(xs_xt['X-t'])

print(headers, payload)
# exit()
response = requests.post(url=url, data=json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8"), headers=headers, verify=False)

print(response.text)
