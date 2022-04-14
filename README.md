# Auto_proxy

利用IP地址池进行自动切换Http代理，防止IP封禁。  
现在蓝狗封IP速度太快了，想想当年自己用Burp爆破封堵IP的日子就想哭。      
不要问我为啥不用飞鱼，太贵了。  

## 支持接口(后续根据反馈进行适量添加)   

- 品易HTTP：http://http.py.cn/  

## 使用指南 

### 购买IP地址池    
推荐余额套餐的方式进行购买，该脚本配合余额支付更划算。  
http://http.py.cn/pay/?paytype=banlance 
![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/1.jpg)
### 获取API接口
购买套餐后，选择》API提取》直接提取，推荐配置如下：（使用时长根据需求自选，提取数量设置为1，默认500，代理协议选Https）
![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/2.jpg)
设置完成后点击》生成API连接》复制链接，将代码复制到auto_proxy.py的py_cn_api参数下；设置监控的网站到auto_proxy.py的ptest_url参数下。 
![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/3.jpg)
运行脚本，python3 auto_proxy.py。
![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/4.jpg)
![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/5.jpg)
## 待优化  
- 仅支持Windows系统 
- 无法同步系统代理到终端    
[![Stargazers over time](https://starchart.cc/Mustard404/Auto_proxy.svg)](https://starchart.cc/Mustard404/Auto_proxy)
