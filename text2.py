from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1000,800")
chrome_options.add_argument("--no-sandbox")
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = {'browser': 'ALL'}
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"')

driver = webdriver.Chrome(chrome_options=chrome_options) # 创建浏览器对象
driver.get('http://www.baidu.com')
print(driver.title)
print('无头浏览器启动成功')
