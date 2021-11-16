from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("window-size=1000,800")
# chrome_options.add_argument("--no-sandbox")
# d = DesiredCapabilities.CHROME
# d['loggingPrefs'] = {'browser': 'ALL'}
# driver = webdriver.Chrome(chrome_options=chrome_options) # 创建浏览器对象
# driver.get('http://www.baidu.com')



# 进入浏览器设置
options = webdriver.ChromeOptions()
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

# options = DesiredCapabilities.CHROME
# options['loggingPrefs'] = {'performance': 'ALL'}
browser = webdriver.Chrome(chrome_options=options)# 创建浏览器对象
browser.get('http://www.baidu.com')


# eles = browser.find_elements_by_xpath("//*[@href]")
# for ele in eles:
#    print(ele.href)
#    print(ele.text)
  
# for entry in browser.get_log('performance'):
#     print(entry)
 
  
print(browser.title)
print('无头浏览器启动成功')
