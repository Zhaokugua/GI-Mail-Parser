import datetime
import base64
import json

# 邮件默认过期时间戳（默认为邮件发送时间+30天）
Mail_default_expire_time = int((datetime.datetime.now() + datetime.timedelta(days=30)).timestamp())

def YSGM_mail(uid, title, sender='PAIMON', expire_time=Mail_default_expire_time, content='This is a Mail.', item_list=None, is_collectible=False):
    """
    生成发送邮件的编码
    :param uid: 要发给的用户的uid
    :param title: 邮件标题
    :param sender: 发送者，默认为PAIMON
    :param expire_time: 过期时间，默认为发送邮件后30天
    :param content: 正文内容，默认为'This is a Mail.'
    :param item_list: 物品列表，默认为空
    item_list = [
        {
            'item_id': 11101,    # 物品id
            'amount': 1,         # 数量
            'level': 90,         # 等级
            'promote_level': 0,  # 突破等级
        },
        {
            'item_id': 11201,  # 物品id
            'amount': 3,  # 数量
            'level': 56,  # 等级
            'promote_level': 1,  # 突破等级
        },
    ]
    :param is_collectible: 是否可以收藏，默认为否
    :return: 返回生成后的字符串
    """
    if item_list:
        item_str = ','.join([f'{x.item_id}:{x.amount}:{x.level}:{x.promote_level}' for x in item_list])
    else:
        item_str = ''
    mail_json = {
        'uid': f'{uid}',
        'title': title,
        'sender': sender,
        'expire_time': f'{expire_time}',
        'content': content,
        'item_list': item_str,
        'is_collectible': is_collectible,
    }
    b64_res = base64.b64encode(bytes(json.dumps(mail_json, ensure_ascii=False, separators=(',', ':')), encoding='utf8'))
    return str(b64_res, encoding='utf8')
 
if __name__ == '__main__':
  result = YSGM_mail(235078418,'test','YSGM',1669215550,'nyan',None,True)
  print(result)
