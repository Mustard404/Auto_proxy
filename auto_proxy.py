import yaml, json, requests, datetime, time
# 测试封禁地址
test_url = "https://sec404.cn/"
# 品易API
py_api = "http://tiqu.pyhttp.taolop.com/getip?count=10&neek=XXXXX&type=2&yys=0&port=11&sb=&mr=1&sep=0&ts=1&ys=1&cs=1&regions=XXXXXX&time=4"
# 设置错误连接次数
max_connect_error = 3

def make_yaml():
    # 读取配置模版
    stream = open('Auto_proxy_example.yaml', 'r')
    clash_conf = yaml.load(stream, Loader=yaml.CLoader)
    stream.close()
    # 请求API，并添加品易返回S5代理
    py_proxy = json.loads(requests.get(py_api).text)
    clash_conf['proxies'] = []
    clash_conf['proxy-groups'][0]['proxies'] = []
    clash_conf['proxy-groups'][1]['proxies'] = []
    for proxy_data in py_proxy['data']:
        proxy = {}
        proxy['name'] = proxy_data['isp'] + "_" + proxy_data['city'] + "_" + proxy_data['ip']
        proxy['type'] = "socks5"
        proxy['server'] = proxy_data['ip']
        proxy['port'] = proxy_data['port']
        clash_conf['proxies'].append(proxy)
        clash_conf['proxy-groups'][0]['proxies'].append(proxy['name'])
        clash_conf['proxy-groups'][1]['proxies'].append(proxy['name'])
    clash_conf['proxy-groups'][0]['url'] = test_url
    clash_conf['proxy-groups'][1]['url'] = test_url
    # 生成新配置文件
    stream = open('Auto_proxy.yaml', 'w', encoding="utf-8")
    yaml.safe_dump(clash_conf, stream, allow_unicode=True)
    stream.close()

def time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 初始化获取ip代理
make_yaml()
# 初始化错误连接数
connect_error = 0
# 测试是否封禁
while True:
    try:
        # 判断代理IP是否被封禁,可根据需求设置timeout值
        resp = requests.get(test_url, timeout=10)
        get_ip = json.loads(requests.get("https://ip.cn/api/index?ip=&type=0", timeout=10).text)
        print( str(time())  + "，OK，公网IP："  + get_ip['ip'] )
        connect_error = 0
    except:
        connect_error = connect_error + 1
        print( str(time()) + "，连接错误次数:" + str(connect_error))
        # 自定义修改错误连接次数
        if connect_error == max_connect_error:
            make_yaml()
            print( str(time())  + "，IP已被封禁，重新获取代理")
            connect_error = 0
            time.sleep(5)

        