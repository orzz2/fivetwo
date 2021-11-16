from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


# 进入浏览器设置
options = webdriver.ChromeOptions()
#----------------


options.add_argument('--log-level=3')
# options.add_argument('--mute-audio')
#---------------
#谷歌无头模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('window-size=1200x600')
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
#设置代理
# if proxy:
#   options.add_argument('proxy-server=' + proxy)
# if user_agent:
#   options.add_argument('user-agent=' + user_agent)

d = DesiredCapabilities.CHROME
# d['loggingPrefs'] = {'performance': 'ALL'}
d["goog:loggingPrefs"] = {'performance': 'ALL'}

#-----------------------------

#-----------------------------

browser = webdriver.Chrome(desired_capabilities=d , chrome_options=options)# 创建浏览器对象
# browser = webdriver.Chrome(desired_capabilities=d)
browser.get('http://www.baidu.com')


# eles = browser.find_elements_by_xpath("//*[@href]")
# for ele in eles:
#    print(ele.href)
#    print(ele.text)
#----------------------------
import json
import time
time.sleep(5)
logs = browser.get_log('performance')

for i in logs:
    log = json.loads(i['message'])
    if log['message']['method'] == 'Network.responseReceived':
#         if log['message']['params']['response']['mimeType'] == 'audio/mp4':
        print(log['message']['params']['response']['url'])
#         addresses.append(log['message']['params']['response']['url'])
# check = set([i.split('/')[-1] for i in addresses])
#---------------------------

 
print('-------------------开始print了！-----------------------')  
print(browser.title)
print('无头浏览器启动成功')
print('-------------------下面是log-----------------------')  
# for entry in browser.get_log('performance'):
#     print(entry)

  
  

print('-------------------this is end-----------------------')  
