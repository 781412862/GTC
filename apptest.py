#coding=utf-8
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'emulator-5556'
#desired_caps['deviceName'] = 'emulator'
desired_caps['appPackage'] = 'com.game.me'
desired_caps['appActivity'] = 'com.being.fame.ui.activity.LaunchActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
#重启
def restart():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#判断页面是否存在
def findItem(el):
    source = driver.page_source
    if el in source:
        return True
    else:
        return False

def harvest(Fname):
    #文件中的用户名读取到列表中
    with open(Fname,'r') as f:
        username = f.read().splitlines()
        #print(username)
        f.close()
    for user in username:
        try:
            print(user)
            driver.find_element_by_id("com.game.me:id/user_name").send_keys(user)
            driver.find_element_by_id("com.game.me:id/password").send_keys('Changeme')
            driver.find_element_by_id("com.game.me:id/login").click()
            #停两秒
            driver.find_element_by_id("com.game.me:id/confirm").click()
            #driver.find_element_by_xpath("//android.widget.ImageView[contains(@text,'游戏星球')]")
            driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'游戏星球')]").click()
            #是否又需要复仇
            #id:com.game.me:id/confirm  text:我要复仇   出现后返回在进入
            time.sleep(5)
            if findItem("你回来了！不好!"):
                driver.back()
            try:
                for gettime in range(0, 2):
                    for i in range(1, 9):
                        elem = "com.game.me:id/reward" + str(i)
                        driver.find_element_by_id(elem).click()
            except  Exception as e:
                print("收完")
            finally:
                driver.back()
            driver.find_element_by_id("com.game.me:id/textView_Name").click()
            driver.find_element_by_id("com.game.me:id/titlebar_right_btn_image").click()
            driver.find_element_by_id("com.game.me:id/logout").click()
        except Exception:
            driver.reset()

while True:
    harvest('debug1.txt')
#退出
#driver.quit()