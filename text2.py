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
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.baidu.com')
print(driver.title)
print('无头浏览器启动成功')
