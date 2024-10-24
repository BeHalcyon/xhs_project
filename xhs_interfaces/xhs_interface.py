import json
import urllib
from urllib.parse import urlencode

import requests

from xhs_interfaces.utils import parse_result
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def comment_request(cookie, note_id, target_comment_id, content, at_users=[]):
    url = "https://edith.xiaohongshu.com/api/sns/web/v1/comment/post"

    # headers = {
    #     'accept': 'application/json, text/plain, */*',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     'origin': 'https://www.xiaohongshu.com',
    #     'priority': 'u=1, i',
    #     'referer': 'https://www.xiaohongshu.com/',
    #     'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    #     'content-type': 'application/json;charset=UTF-8'
    # }
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://www.xiaohongshu.com',
        'priority': 'u=1, i',
        'referer': 'https://www.xiaohongshu.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-b3-traceid': '92008d787b241500',
        'x-s-common': '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',
        'x-xray-traceid': 'c95edd6da5f9962343c341e6d9c4b3b7',
        # 'Cookie': 'a1=18d5fae5576zwcukigljfy0aaw0ady2k1e847m5ph30000294564; webId=e11488368087c8ef20861064f4caaa7c; gid=yYf2i0d2DDyDyYf2i0d22d62WKuES7T3k1ViYUxv800E84q80fvJTW888Jj42K48Dq4Kd4dJ; abRequestId=e11488368087c8ef20861064f4caaa7c; web_session=0400698ed6dc9256561e2a222d354ba12b8619; customer-sso-sid=68c517428807402125437553b99877216c27ffc6; x-user-id-creator.xiaohongshu.com=5fa29fda0000000001000648; customerClientId=616596286637831; access-token-creator.xiaohongshu.com=customer.creator.AT-68c5174288074021254375540vzakx5ppofte9mg; galaxy_creator_session_id=GSUX3DrW3ZfZHdeYVF6dwMQ7mWBaTTXgWBDh; galaxy.creator.beaker.session.id=1729654009085019524796; xsecappid=xhs-pc-web; unread={%22ub%22:%22671772140000000021008975%22%2C%22ue%22:%226717bba5000000001402ed5b%22%2C%22uc%22:29}; webBuild=4.40.3; websectiga=82e85efc5500b609ac1166aaf086ff8aa4261153a448ef0be5b17417e4512f28; sec_poison_id=24eb7c17-fbad-4e53-b571-ba5e2c673707; acw_tc=481305b34d7195217425d438611ae391cdd758a5ebc17dd81cf6740dab28d4d0',
        'content-type': 'application/json;charset=UTF-8'
    }

    payload = {
        "note_id": note_id,
        "content": content,
        # "target_comment_id": target_comment_id,
        "at_users": at_users
    }
    if target_comment_id:
        payload['target_comment_id'] = target_comment_id
    api = url[url.find("/api"):]

    xs_xt = parse_result(api, cookie, payload)

    headers['Cookie'] = cookie
    headers['X-s'] = xs_xt['X-s']
    headers['X-t'] = str(xs_xt['X-t'])

    response = requests.post(url=url,
                             data=json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8"),
                             headers=headers, verify=False)

    return response.json()


def article_list_request(cookie, category="homefeed.fashion_v3"):
    url = "https://edith.xiaohongshu.com/api/sns/web/v1/homefeed"

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

    payload = {
        "cursor_score": "",
        "num": 18,
        "refresh_type": 1,
        "note_index": 18,
        "unread_begin_note_id": "",
        "unread_end_note_id": "",
        "unread_note_count": 0,
        "category": category,
        "search_key": "",
        "need_num": 8,
        "image_formats": [
            "jpg",
            "webp",
            "avif"
        ],
        "need_filter_image": False
    }

    api = url[url.find("/api"):]

    xs_xt = parse_result(api, cookie, payload)
    # print(xs_xt)

    headers['cookie'] = cookie
    headers['X-s'] = xs_xt['X-s']
    headers['X-t'] = str(xs_xt['X-t'])

    response = requests.post(url=url,
                             data=json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8"),
                             headers=headers, verify=False).json()
    # 获取到一批文章id
    note_infos = []
    # print(response)

    for item in response['data']['items']:

        note_infos.append({
            "note_id": item['id'],
            "xsec_token": item['xsec_token']
        })
        # print(note_infos[-1])


    return note_infos

def post_feed_by_note_id(cookie, note_id, xsec_source="pc_search", xsec_token = None):
    url = "https://edith.xiaohongshu.com/api/sns/web/v1/feed"

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

    payload = {
        "source_note_id": note_id,
        "image_formats": [
            "jpg",
            "webp",
            "avif"
        ],
        "extra": {
            "need_body_topic": "1"
        },
        "xsec_source": xsec_source,
        "xsec_token": xsec_token
    }

    api = url[url.find("/api"):]

    xs_xt = parse_result(api, cookie, payload)
    # print(xs_xt)

    headers['cookie'] = cookie
    headers['X-s'] = xs_xt['X-s']
    headers['X-t'] = str(xs_xt['X-t'])

    response = requests.post(url=url,
                             data=json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8"),
                             headers=headers, verify=False).json()
    print(response)
    return response['data']['items'][0]



cookie = "a1=18d5fae5576zwcukigljfy0aaw0ady2k1e847m5ph30000294564; webId=e11488368087c8ef20861064f4caaa7c; gid=yYf2i0d2DDyDyYf2i0d22d62WKuES7T3k1ViYUxv800E84q80fvJTW888Jj42K48Dq4Kd4dJ; abRequestId=e11488368087c8ef20861064f4caaa7c; webBuild=4.39.0; web_session=0400698ed6dc9256561e2a222d354ba12b8619; customer-sso-sid=68c517428807402125437553b99877216c27ffc6; x-user-id-creator.xiaohongshu.com=5fa29fda0000000001000648; customerClientId=616596286637831; access-token-creator.xiaohongshu.com=customer.creator.AT-68c5174288074021254375540vzakx5ppofte9mg; galaxy_creator_session_id=GSUX3DrW3ZfZHdeYVF6dwMQ7mWBaTTXgWBDh; galaxy.creator.beaker.session.id=1729654009085019524796; xsecappid=xhs-pc-web; unread={%22ub%22:%2267178f1f0000000024017f3d%22%2C%22ue%22:%2266f91620000000002c014693%22%2C%22uc%22:31}; websectiga=10f9a40ba454a07755a08f27ef8194c53637eba4551cf9751c009d9afb564467; sec_poison_id=8b7f7622-3de3-4167-9a83-75728182cdef; acw_tc=79acb76835b9945c1de487766e6b2a6d08636bba1d2c799d73fa632a6d816f6d"
# note_infos = article_list_request(cookie)
# print(note_infos)
# exit()

def get_comment_request(cookie, note_id, xesc_token):

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

    payload = {
        "note_id": note_id,
        "cursor": "",
        "top_comment_id": "",
        "image_formats": "jpg,webp,avif",
        "xsec_token": xesc_token
    }

    host = "https://edith.xiaohongshu.com"
    uri = "/api/sns/web/v2/comment/page"
    final_uri = f"{uri}?{urlencode(payload)}"

    xs_xt = parse_result(final_uri, cookie, None)

    headers['cookie'] = cookie
    headers['X-s'] = xs_xt['X-s']
    headers['X-t'] = str(xs_xt['X-t'])
    url = f"{host}{uri}"
    response = requests.get(url=url, params=payload, headers=headers, verify=False).json()

    # 获取到评论id、评论内容、note_id等
    comments = []
    for comment in response['data']['comments']:
        comments.append({
            "comment_id": comment['id'],
            "content": comment['content'],
            "like_count": comment['like_count'],
        })
        # print(comments[-1])

    return comments

# note_id = "670f6c26000000002401a13d"
# xesc_token = "ABk5lPiokSY81_AzrQbJjXHN0C9pxLOGnyB6u93hYoO5w="
# # get_comment_request(cookie, note_id, xesc_token)
# note_content = post_feed_by_note_id(cookie, note_id, xsec_token = xesc_token)
# print(note_content)