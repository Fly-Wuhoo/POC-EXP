# 影响范围：
OneBlog <= v2.2.1
# FOFa dork：
app="OneBlog开源博客后台管理系统"
# 漏洞复现：
登录页面：
![image](images/login.png)
由于OneBlog小于2.2.1版本中使用了存在漏洞版本的Apache Shiro及默认密钥导致存在远程代码执行漏洞，使用shiro反序列化工具进行利用。
![image](images/key.png)
成功反弹shell
![image](images/shell.png)
![image](images/success.png)
