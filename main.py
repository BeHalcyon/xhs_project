import random
import time

from xhs_interfaces.utils import print_format
from gpt.qwen.comment_assistant import QwenMaxCommentAssistant
from xhs_interfaces.xhs_field import FeedType
from xhs_interfaces.xhs_interface import *

def comment_test():
    cookie = "a1=18d5fae5576zwcukigljfy0aaw0ady2k1e847m5ph30000294564; webId=e11488368087c8ef20861064f4caaa7c; gid=yYf2i0d2DDyDyYf2i0d22d62WKuES7T3k1ViYUxv800E84q80fvJTW888Jj42K48Dq4Kd4dJ; abRequestId=e11488368087c8ef20861064f4caaa7c; webBuild=4.39.0; web_session=0400698ed6dc9256561e2a222d354ba12b8619; customer-sso-sid=68c517428807402125437553b99877216c27ffc6; x-user-id-creator.xiaohongshu.com=5fa29fda0000000001000648; customerClientId=616596286637831; access-token-creator.xiaohongshu.com=customer.creator.AT-68c5174288074021254375540vzakx5ppofte9mg; galaxy_creator_session_id=GSUX3DrW3ZfZHdeYVF6dwMQ7mWBaTTXgWBDh; galaxy.creator.beaker.session.id=1729654009085019524796; acw_tc=1824b0a96f9c5b8241104e795345716176374d70bc029838396fb3b90bb9f5ee; xsecappid=xhs-pc-web; websectiga=82e85efc5500b609ac1166aaf086ff8aa4261153a448ef0be5b17417e4512f28; sec_poison_id=2595d4dd-7d59-40b9-baa7-74e221d0d320; unread={%22ub%22:%22670714af000000002c0164ee%22%2C%22ue%22:%226707ce40000000001902d58b%22%2C%22uc%22:12}"  # put your cookie here
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


    #     article = """
#     自我维权后发现了比12315更棒的退费方法
# ⏩之前我发了关于退费的笔记，得到了许多姐妹的关注，后续也和许多姐妹进行了退费相关的沟通。了解了上百位姐妹们的案例流程后，得到了此高交攵率版本的维权流程。⏹
# .
# ⏩.亻言访局投诉。操作流程在后面配图➡️ ⏩不否认12345、12315、黑猫的投诉功能，姐妹们也可以同时投诉这三个平台。⏺
# .
# ⏩只是数据告诉我亻言访局的受理率与解决成功率是蕞高的，12315、12345和黑猫很容易没有后续。
# .
# 🆗有目的的与机构沟通。言语中透露自己已经给各大平台投诉的亻言息，不需要和机构进行过多的纠缠，它们很会装糊涂狡辩，别到时候惹得自己一肚子气。⏺
# .
# 🆗静候亻言访局的消息。已受理后大概会等待10个工作日，有回访电话。一般这个时候机构会主动来找你进行退费的相关沟通。✨
# .
# ⚠️假如投诉无门，选择线上诉讼🌟🌟
# .
# 💁了解了上百位姐妹们的案例流程后，得到了此高交攵率版本的维权流程。有什么不懂的可关注厚苔踢踢给个肖息哈🔁
# .
# #自我保护#法律咨询#退费维权#退费#小红书法律知识课堂#培训机构退费#医疗美容退费#健身房退费#12315消费者维权投诉#网课退费 #自考 #网课分期取消"""
#     comments = [
#         "我笔记下面截🐮很多，但凡说推靠谱，己追回的，己退可帮，主动丝妮的请谨慎辨别，都是托己有粉粉二次被遍哈",
#         "✅不论是报了什么培训班，补习班、兴趣班，办了任何美容卡、健身卡，只要你中途不想去了，即便是个人原因也是可以退费！可以退款！可以退卡的！重要的事情说三遍！！！",
#         "办的祛痘套餐，每个月缴一定金额，现在不想去了，能停止缴费吗？上个月一次没去也是照样扣我的钱",
#         "你好杨律师，好有缘我也姓杨，我想咨询一下，我今天脑子一抽去做了小说接单需要380元，我一下就给她转过去了那时候11点，现在我越想越感觉我没了380心里没有谱了，我还是学生，380元快够我一个月的生活费了，我要她给我退款，她不给我退，我该怎么办啊，杨律师",
#         "网上买的画画课，她们让我签合同了，一次没上可以解约吗，她们让我赔付20%"
#     ]
#     target_comment = QwenMaxCommentAssistant.query_comment(article, comments)
#     print_format(f"target comment: {target_comment}")
#
#     note_id = "66fc0fd7000000002a0321e7"
#     target_comment_id = None
#
#     print_format("ready to comment...")
#     comment_response = comment_request(cookie, note_id, target_comment_id, target_comment, at_users=[])
#     print_format(f"comment result: {comment_response}")



if __name__ == '__main__':
    comment_test()
