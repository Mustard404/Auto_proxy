import winreg
import ctypes
import requests
import time
import json


# API设置
py_cn_api = "http://tiqu.pyhttp.taolop.com/getip?count=1&neek=XXXX&type=2&yys=0&port=2&sb=&mr=1&sep=0&ts=1&time=2"
test_url = "https://sec404.cn/"

# 如果从来没有开过代理 有可能健不存在 会报错
INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                   r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                   0, winreg.KEY_ALL_ACCESS)
# 设置刷新
INTERNET_OPTION_REFRESH = 37
INTERNET_OPTION_SETTINGS_CHANGED = 39
internet_set_option = ctypes.windll.Wininet.InternetSetOptionW


def set_key(name, value):
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

# 启用代理
def start(proxy_server):
    set_key('ProxyEnable', 1) 
    set_key('ProxyOverride', u'*.local;<local>') # 绕过本地
    set_key('ProxyServer', proxy_server) 
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0,INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
# 停用代理

def stop():
    set_key('ProxyEnable', 0)
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
    print('代理已关闭')

# 防止代理开启干扰导致接口白名单错误


# 品易API
def py_cn():
    stop()
    proxy = json.loads(requests.get(py_cn_api).text)['data'][0]
    proxyMeta = "http://%(host)s:%(port)s" % {
        "host" : proxy['ip'],
        "port" : proxy['port'],
    }
    proxies = {
        "http" : proxyMeta,
        "https" : proxyMeta
    }
    start(str(proxy['ip']) + ':' + str(proxy['port']))
    print("已设置当前IP为:" + proxy['ip'] )
    return proxies

proxy_status = py_cn()

while True:
    # 设置刷新
    try:
        # 判断代理IP是否被封禁,可根据需求设置timeout值
        resp=requests.get(test_url, proxies=proxy_status, timeout=10)
        print("OK," + str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))

    except:
        print("IP已被封禁，停止代理")
        proxy_status = py_cn()