#coding=utf-8
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Android Emulator'
#desired_caps['deviceName'] = 'emulator'
desired_caps['appPackage'] = 'com.game.me'
desired_caps['appActivity'] = 'com.being.fame.ui.activity.LaunchActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(8)
#判断页面是否存在
def findItem(el):
    source = driver.page_source
    if el in source:
        return True
    else:
        return False

def edittextclear(self, text):

        '''

       请除EditText文本框里的内容

        @param:text 要清除的内容

        '''
        driver.keyevent(123)

        for i in range(0, len(text)):
            driver.keyevent(67)
#自动注册
def singIn(times,nowN):
    driver.swipe(600,900,100,900,900)
    for i in range(times):
        uName = "gu78141" + str(nowN + i)
        emali = "gu78141" + str(nowN + i)+"@qq.com"
        driver.find_element_by_id("com.game.me:id/username").send_keys(uName)
        driver.find_element_by_id("com.game.me:id/login").click()
        driver.find_element_by_id("com.game.me:id/edit_pwd").send_keys("Changeme")
        driver.find_element_by_id("com.game.me:id/edit_email").send_keys(emali)
        driver.find_element_by_id("com.game.me:id/reg").click()
        driver.find_element_by_id("com.game.me:id/back").click()
        driver.find_element_by_id("com.game.me:id/back").click()
        el = driver.find_element_by_id("com.game.me:id/username")
        el.click()
        #清除文本框内容
        for i in range(0, len(uName)):
            driver.keyevent(67)
        print("目前账号为：%s"%uName)

        file = open('username.txt', 'a')
        file.write('\n'+uName)
        file.close()
#偷别人的能量，加在已登录后面调用
def otherget():
    try:
        for a in range(1, 12):
            if findItem("com.game.me:id/confirm"):
                driver.find_element_by_id("com.game.me:id/confirm").click()
                break
            elif findItem("com.game.me:id/lottieAnim"):
                driver.find_element_by_id("com.game.me:id/exchange").click()
            else:
                elem = "com.game.me:id/reward1"
                driver.find_element_by_id(elem).click()
                driver.find_element_by_id("com.game.me:id/exchange").click()
    except  Exception as e:
        for a in range(1, 5):
            if findItem("com.game.me:id/confirm"):
                driver.find_element_by_id("com.game.me:id/confirm").click()
                break
            elif findItem("com.game.me:id/lottieAnim"):
                driver.find_element_by_id("com.game.me:id/exchange").click()
            else:
                elem = "com.game.me:id/reward1"
                driver.find_element_by_id(elem).click()
                driver.find_element_by_id("com.game.me:id/exchange").click()
    finally:
        driver.back()
    try:
        driver.find_element_by_id("com.game.me:id/backBtn").click()
    except Exception:
        driver.back()

def GameStart(filename):
    with open(filename, 'r') as f:
        username = f.read().splitlines()
        # print(username)
        f.close()
    for user in username:
        try:
            print(user)
            driver.find_element_by_id("com.game.me:id/user_name").send_keys(user)

            driver.find_element_by_id("com.game.me:id/password").send_keys('Changeme')

            driver.find_element_by_id("com.game.me:id/login").click()
            time.sleep(3)
            driver.find_element_by_id("com.game.me:id/confirm").click()
            # driver.find_element_by_xpath("//android.widget.ImageView[contains(@text,'游戏星球')]")
            driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'游戏星球')]").click()
            time.sleep(3)
            if findItem("我要复仇"):
                driver.back()
            try:
                driver.find_element_by_id("com.game.me:id/confirm").click()
            except Exception:
                #账号已开启星球
                pass
            driver.find_element_by_id("com.game.me:id/visit").click()
            #偷能量
            otherget()
            driver.find_element_by_id("com.game.me:id/textView_Name").click()
            driver.find_element_by_id("com.game.me:id/titlebar_right_btn_image").click()
            driver.find_element_by_id("com.game.me:id/logout").click()
        except Exception:
            driver.reset()


GameStart("usernameDebug.txt")
#singIn(510,33526)




