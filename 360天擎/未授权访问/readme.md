# 影响范围：
360天擎
# FOFa dork：
app="360新天擎"
# 漏洞复现：
登录页面：
![image](images/login.png)
漏洞地址：/api/dbstat/gettablessize  
burp抓包可以看到成功返回数据库表名等信息  
![image](images/burp.png)  
通过浏览器访问 
![image](images/success.png)
使用脚本批量检测：  
![image](images/script.png)

