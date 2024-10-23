import json
import os
import re
import execjs
import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}


def transferCookies(cookies):
    cookiesList = cookies.split(';')
    cookiesJs = []
    for value in cookiesList:
        if value == "":
            continue
        cookiesJs.append(value)
    return cookiesJs



def parsResult(e, cookies, t=None):
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "xhs_decrypt.js")
    print(e, json.dumps(t), transferCookies(cookies))
    return execjs.compile(open(file_path, 'r', encoding='utf-8').read()).call('XsXt', e, t, transferCookies(cookies))


def sentPostRequest(host, api, data, cookie):
    if cookie == "":
        print("need cookie")
        return

    xs_xt = parsResult(api, cookie, data)

    headers['cookie'] = cookie
    headers['X-s'] = xs_xt['X-s']
    headers['X-t'] = str(xs_xt['X-t'])

    url = host + api
    response = requests.post(url=url, data=json.dumps(data, separators=(",", ":"), ensure_ascii=False).encode("utf-8"), headers=headers, verify=False)

    return response.json()
def DoApi(param, cookie):
    api = '/api/sns/web/v1/comment/post'
    host = 'https://edith.xiaohongshu.com'
    data = {
        "note_id": param["note_id"],
        "content": param["content"],
        "at_users":  param["at_users"],
    }
    return sentPostRequest(host, api, data, cookie)




if __name__ == '__main__':
    # 向笔记发送评论demo
    # warning 该js逆向只能用于改接口，如需其他接口请联系作者

    cookie = "xsecappid=xhs-pc-web; a1=18dfad38995dqrlj5gm1jba0u2ve1oe9drlpvae6150000392391; webId=33726a7a9a13de412bb7ce4d261fefa0; gid=yYfi0fqYDYfDyYfi0fqYjF0dj2fAF1V2k6yV1KyD087JhU28dyldjh888qjJqjy8fYjjdjy2; abRequestId=33726a7a9a13de412bb7ce4d261fefa0; webBuild=4.39.0; websectiga=cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c; sec_poison_id=4ed1077d-29bf-41c9-8366-f969515c4b61; acw_tc=0cf569802356201734afe4140df53b1c6596ec639782cbc72c7e015b22a0670a; web_session=0400698ed6dc9256561e5a8522354b06ac97bd; unread={%22ub%22:%226704f702000000002a0331c9%22%2C%22ue%22:%2266fa8f20000000002c01661c%22%2C%22uc%22:28}" # put your cookie here
    param = {
        "note_id": "64e1d603000000001700f40d",
        "content": "hello world",
        "at_users":  []
    }

    response = DoApi(param,cookie)
    print(response)