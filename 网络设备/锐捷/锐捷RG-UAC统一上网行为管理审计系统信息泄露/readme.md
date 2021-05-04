# 影响范围：
锐捷RG-UAC统一上网行为管理审计系统
# FOFa dork：
title="RG-UAC登录页面" && body="admin"  
# 漏洞复现：
登录页面：
![image](images/login.png)
Ctrl+U查看源码，搜索```password```关键字，获取账号和密码md5值。
![image](images/passwd.png)
使用md5解密网站解密  
![image](images/md5.png)
使用获得的账号密码成功登录系统：  
![image](images/success.png)


