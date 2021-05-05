# 影响范围：
锐捷EG易网关
# FOFa dork：
app="Ruijie-EG易网关"
# 漏洞复现：
登录页面：
![image](images/index.png)
此漏洞需要成功登录系统才能成功利用，可以结合管理员账号密码泄露漏洞获取管理员账号密码登录系统进一步进行漏洞利用。     
登录系统
![image](images/login.png)
登录成功后请求如下地址， file参数设置为需要查看的文件，可以使用 ../ 跳转目录：
![image](images/read.png)
使用脚本进行批量验证，本脚本结合了管理员账号泄露漏洞，自动获取账号密码并进行漏洞检测：  
![image](images/script.png)


