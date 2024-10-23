import random
import time

from xhs_interfaces.utils import print_format
from gpt.qwen.comment_assistant import QwenMaxCommentAssistant
from xhs_interfaces.xhs_field import FeedType
from xhs_interfaces.xhs_interface import *

def comment_test():
    # 17682323970
    cookie = "a1=18d5fae5576zwcukigljfy0aaw0ady2k1e847m5ph30000294564; webId=e11488368087c8ef20861064f4caaa7c; gid=yYf2i0d2DDyDyYf2i0d22d62WKuES7T3k1ViYUxv800E84q80fvJTW888Jj42K48Dq4Kd4dJ; abRequestId=e11488368087c8ef20861064f4caaa7c; webBuild=4.39.0; web_session=0400698ed6dc9256561e2a222d354ba12b8619; customer-sso-sid=68c517428807402125437553b99877216c27ffc6; x-user-id-creator.xiaohongshu.com=5fa29fda0000000001000648; customerClientId=616596286637831; access-token-creator.xiaohongshu.com=customer.creator.AT-68c5174288074021254375540vzakx5ppofte9mg; galaxy_creator_session_id=GSUX3DrW3ZfZHdeYVF6dwMQ7mWBaTTXgWBDh; galaxy.creator.beaker.session.id=1729654009085019524796; acw_tc=1824b0a96f9c5b8241104e795345716176374d70bc029838396fb3b90bb9f5ee; xsecappid=xhs-pc-web; websectiga=82e85efc5500b609ac1166aaf086ff8aa4261153a448ef0be5b17417e4512f28; sec_poison_id=2595d4dd-7d59-40b9-baa7-74e221d0d320; unread={%22ub%22:%22670714af000000002c0164ee%22%2C%22ue%22:%226707ce40000000001902d58b%22%2C%22uc%22:12}"  # put your cookie here

    # 16638143970
    cookie = "abRequestId=14794d6b-b799-5f27-af00-cea84bc4bfff; webBuild=4.40.2; xsecappid=xhs-pc-web; a1=192ba09760cxdltwopebh57q5djf4pbjqsqtv41yi50000226449; webId=d17a290f39792fe352318aae94eb9878; websectiga=29098a4cf41f76ee3f8db19051aaa60c0fc7c5e305572fec762da32d457d76ae; sec_poison_id=07dabe4b-7368-4357-b502-7fab538a4de1; acw_tc=52f221185a8fe4154af8d27529f7cbc3b13cb6c21228e6964797149caa3a64b9; gid=yjJD08jY8SAqyjJD08jWKM4y8SCf19ElUdDxAv32WA2fV928i4UDVh888JJK44j8y4fKWJiq; web_session=0400698e590ea3566e3949512c354bcaffc385; unread={%22ub%22:%226713cdae0000000016023c83%22%2C%22ue%22:%2267166d6b000000002100804c%22%2C%22uc%22:28"

    print_format("load comment...")

    ## 根据分类刷文章
    articles = article_list_request(cookie, category=FeedType.EMOTION.value)
    # "homefeed.love_v3"
    print_format(f"All articles count: {len(articles)}")
    for index, item in enumerate(articles):
        note_id, xsec_token = item['note_id'], item['xsec_token']
        link = f"https://www.xiaohongshu.com/explore/{note_id}?xsec_token={xsec_token}&xsec_source=pc_feed&source=xhs_sec_server"
        print_format(f"[{index+1}/{len(articles)}] start to comment note_id: {note_id}, link: {link}")
        note_content = post_feed_by_note_id(cookie, note_id, xsec_token=xsec_token)
        note_title = "标题：" + note_content['note_card']['title']
        note_desc = "内容：" + note_content['note_card']['desc']
        comments = get_comment_request(cookie, note_id, xsec_token)
        article = note_title + "\t" + note_desc
        print_format(f"[{index+1}/{len(articles)}] note content: {article}")

        i = 0
        comment_buf_list = []
        for comment_item in comments:
            comment_id, comment_content, like_count = comment_item['comment_id'], comment_item['content'], comment_item['like_count']
            print_format(f"[{index+1}/{len(articles)}] comment_id: {comment_id}, content: {comment_content}, like_count: {like_count}")
            comment_buf_list.append(comment_content)
            if i >= 8:
                break

        target_comment = QwenMaxCommentAssistant.query_comment(article, comments)
        print_format(f"[{index+1}/{len(articles)}] target comment: {target_comment}")

        # note_id = "66fc0fd7000000002a0321e7"
        target_comment_id = None

        print_format(f"[{index+1}/{len(articles)}] ready to comment...")
        comment_response = comment_request(cookie, note_id, target_comment_id, target_comment, at_users=[])
        print_format(f"[{index+1}/{len(articles)}] comment result: {comment_response}")
        sleep_time = random.randint(60, 80)
        print_format(f"[{index+1}/{len(articles)}] sleep time: {sleep_time}s.")
        time.sleep(sleep_time)





if __name__ == '__main__':
    for i in range(24):
        comment_test()
