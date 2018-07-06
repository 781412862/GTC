from appium import webdriver
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Android Emulator'
#desired_caps['deviceName'] = 'emulator'
desired_caps['appPackage'] = 'com.game.me'
desired_caps['appActivity'] = 'com.being.fame.ui.activity.LaunchActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def writFil(filename,way,number):
    #用户名写入文件
    #增加个数j
    #写入值value
    file = open(filename,way)
    for i in range(0,number):
        value = "gu78141" + str(2860+i)+"\n"
        file.write(value)
    file.close()
# 等待直到元素出现, 点击

def waitClick(self, time, element):
    try:
        #print('元素加载, 页面等待中 ...')
        WebDriverWait(self.driver,time).until(EC.presence_of_element_located((By.ID,element)),
                                              message='not find')
    except Exception as e:
        print('没有找到元素 %s :'%element)

# with open('username.txt','r',encoding='gbk') as f:
#     # for line in f:
#     #     print(line,end='')
#     #有换行符
#     # content = list(f)
#     #去掉换行符
#     content = f.read().splitlines()
#     print(content)
#
#     f.close()
writFil('username.txt','w',170)





