import os
import execjs
import datetime


def transfer_cookies(cookies):
    cookies_list = cookies.split(';')
    cookies_js = []
    for value in cookies_list:
        if value == "":
            continue
        cookies_js.append(value)
    return cookies_js


def parse_result(e, cookies, t=None):
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "xhscrawl/xhs_decrypt.js")
    # 设置工作目录
    working_directory = os.path.join(current_directory, "xhscrawl")
    os.chdir(working_directory)
    return execjs.compile(open(file_path, 'r', encoding='utf-8').read()).call('XsXt', e, t,
                                                                              transfer_cookies(cookies))


def print_format(str):
    print(f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {str}')
