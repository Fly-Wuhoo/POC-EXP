# 影响范围：
佑友防火墙
# FoFa Dork
title="佑友防火墙"
# 漏洞复现：
登录页面：
![image](images/login.png)
使用默认账号密码登录：  
```
账号：admin
密码：hicomadmin
```
选择 系统管理——维护工具——ping
![image](images/ping.png)  
在目的地址框内通过使用管道符进行命令执行：  
执行whoami：  
![image](images/whoami.png)    
查看passwd文件
![image](images/passwd.png)  
