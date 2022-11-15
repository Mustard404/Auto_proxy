# Auto_proxy V2

利用Python脚本自动生成Clash配置文件，实现FUZZ自动切换IP。  
现在蓝狗封IP速度太快了，想想当年自己用Burp爆破封堵IP的日子就想哭。      
不要问我为啥不用飞鱼，太贵了。  

## 支持接口(后续根据反馈进行适量添加)   

- 品易HTTP：http://http.py.cn/  

## 使用指南 

### 购买IP地址池    

推荐余额套餐的方式进行购买，该脚本配合余额支付更划算(以下链接注册可赠送免费测试)。  
[http://http.py.cn/?utm-source=wxwx&utm-keyword=?0001](http://http.py.cn/?utm-source=wxwx&utm-keyword=?0001)

### 获取API接口
购买套餐后，选择》API提取》直接提取，推荐配置如下：
- 1.余额提取。      
- 2.使用时长按需选择，建议选择25分钟-180分钟。  
- 3.提取数量建议为5-10，土豪随意。  
- 4.建议省份混拨，并选择自己所在省份或临近省份，提高访问速度。  
- 5.目前该代理协议仅支持SOKCS5连接。    
- 6.数据格式选择Json格式，方便脚本解析。    
- 7.选择属性全部勾选，否则会发生错误。  
- 8.IP去重365天。   

![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/1.jpg)     

### 部署说明
将Auto_proxy代码（Auto_proxy_example.yaml, Auto_proxy.py, proxyIgnoreList.plist ）拷贝到Clash配置文件目录下。   

- Windows默认：Clash\Data\profiles\
- Mac默认：~/.config/clash/

![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/2.jpg)     

修改Auto_proxy.py相关配置，主要参数如下。    

- test_url：需要监控测试的IP地址。
- py_api：上一步获取的品易API接口。
- max_connect_error：错误连接次数，连续连接错误N次，重新获取代理。
 
 ![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/3.jpg)  

白名单配置，可参考https://www.cnblogs.com/PowerTips/p/14775956.html

- Windows：在Auto_proxy_example.yaml添加cfw-bypass配置。    
- Mac: 直接使用项目中proxyIgnoreList.plist即可，需重启生效。    

注：务必将*.taolop.com加入白名单中，不然可能会导致代理失效一直重复获取代理。    

### 使用说明
在Clash目录下执行python3 Auto_proxy.py，同时Clash将配置选为Auto_proxy。 

 ![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/4.jpg)    

需将Clash配置为全局模式，同时设置系统代理，目前脚本设置两种规则：   

- 加速模式：根据监控网站选择延迟最低的代理。    
- 负载模式：每次请求都会随机一条代理进行连接。  

 ![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/5.jpg)    

负载模式运行效果：  

![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/6.jpg)     

当运行错误超出设置阀值，会进行提示“IP已被封禁，重新获取代理”，此时Clash提示“重载配置文件”，需手动点击更新。 

![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/7.jpg)     

### 使用效果

该效果模式为负载模式，测试Dirsearch, 其它工具请自行测试。   
- 靶机端： python3 -m http.server 8000  
- 攻击端： python3 dirsearch.py -u  http://X.X.X.X:8000 --proxy=http://127.0.0.1:7890   

![image](https://github.com/Mustard404/Auto_proxy/blob/main/demo/8.jpg) 

🤣 🤣 🤣  同时10个IP爆破目录，就问你慌不慌！

### 参考文档

- [ClashX 配置代理白名单](https://www.cnblogs.com/PowerTips/p/14775956.html)
- [Clash实现IP秒级切换](https://segmentfault.com/a/1190000040828310)


## Stargazers over time 

[![Stargazers over time](https://starchart.cc/Mustard404/Auto_proxy.svg)](https://starchart.cc/Mustard404/Auto_proxy)


