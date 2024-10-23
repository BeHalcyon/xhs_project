from openai import OpenAI

class QwenMaxCommentAssistant():

    comment_prompt: str = None

    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key="sk-8d80e99d41df4eceb6b2c1071d4e1a6c",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    def __init__(self):
        pass

    @classmethod
    def load_prompt_template(cls):
        with open("./comment_prompt.txt", 'r', encoding='utf-8') as file:
            content = file.read()
        cls.comment_prompt = content

    @classmethod
    def composite_prompt(cls, article, comments):
        if not cls.comment_prompt:
            cls.load_prompt_template()

        if not comments or len(comments) == 0:
            comments = "无评论"
        else:
            comments = "\n".join([f"{i}. {comment}" for i, comment in enumerate(comments)])

        current_comment_prompt = cls.comment_prompt.\
            replace("{{query}}", article).\
            replace("{{comments}}", comments)

        return current_comment_prompt

    @classmethod
    def query_comment(cls, article, comments):
        current_comment_prompt = cls.composite_prompt(article, comments)
        completion = cls.client.chat.completions.create(
            model="qwen-max-latest",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            messages=[
                # {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': current_comment_prompt}],
        )
        print(completion.model_dump_json())

if __name__ == "__main__":
    article = "始终不明白，为何出价100万了，老父亲都不肯卖掉！ #自然奇观  #奇闻趣事  #户外旅行  #乡村风景  #航拍最美家乡"
    comments = [
        "我们乡下随便盖栋房子都100w",
        "住这不比住挤在城里那几十平米好吗？城里你花100万买了啥，买的天花板是楼上的地面，买的地面是楼下的天花板，最终也就买了个门而已，而且每年都要交物业费",
        "靠山石",
        "风水已经被人破了，这个原来应该是一整块，好像是为了开路把它给挖断了，有人使坏，特地给它头上钉了几根桩子",
        "我老家房子也这样，旁边被我爸用炸药加肩挑手扛挖平了"
    ]
    QwenMaxCommentAssistant.query_comment(article, comments)