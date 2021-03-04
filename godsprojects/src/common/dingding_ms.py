# coding=utf-8
'''
Author:wangmin
Date:2021.2.24
'''


import time
import hmac
import hashlib
import base64
import urllib
import sys
import requests,json   #导入依赖库
from numpy import long




#encryption
timestamp = str(round(time.time() * 1000))
secret = 'SEC7cf8c2c586e7d0ca1ac2a7f233a1d3491d8762e23feea813cadab8b362f68bad'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)


#  张雪0，唐枣锥1，施继峰2，蔡璐璐3，陈敏清4，王敏5
mobiles = ['18605886945','15889735883','15757185534','13735428651','18768143563','13758206408']
headers={'Content-Type': 'application/json'}   #定义数据类型
#webhook = 'https://oapi.dingtalk.com/robot/send?access_token=a0f49efa43ec4a009dfa493c38af46ffd36c4e72ae455c3b84849752a1c75490&timestamp='+ str(timestamp)+"&sign="+sign
#测试群的机器人
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=43174ee6e8cb81d5d6b36bfe209232758659a4b633a9146758734a93a098c4a2&timestamp='+ str(timestamp)+"&sign="+sign


class Dingtalk():
    def __init__(self):
        print("start!")

    def ding_talk(self):

        try:
            mobile = []
            mobile.append(mobiles[2])
            mobile.append(mobiles[5])
            #title = "UI"

            print(mobile)

            data = {
                "msgtype": 'text',
                "text": {
                    "content": "ui自动化测试报告已生成 "
                },
                "at": {
                    "atMobiles": mobile,
                    "isAtAll": False
                }
            }

            res = requests.post(webhook, data=json.dumps(data), headers=headers)  # 发送post请求
            print(res.text)

        except Exception as e:
            print(repr(e))
        except:
            print ("unknow error!")

if __name__ == '__main__':
    dingtalk = Dingtalk()
    #dingtalk.ding_talk('20200902111336', 'dksc_测试报错脚本接口回归.jmx')
    #dingtalk.ding_talk(sys.argv[1],sys.argv[2])
    dingtalk.ding_talk()