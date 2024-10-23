import json
import urllib
from urllib.parse import urlencode

import requests

from xhs_interfaces.utils import parse_result
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def comment_request(cookie, note_id, target_comment_id, content, at_users=[]):
    url = "https://edith.xiaohongshu.com/api/sns/web/v1/comment/post"

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
        "content": content,
        "target_comment_id": target_comment_id,
        "at_users": at_users
    }
    api = url[url.find("/api"):]

    xs_xt = parse_result(api, cookie, payload)

    headers['cookie'] = cookie
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