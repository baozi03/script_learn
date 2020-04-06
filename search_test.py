def sesrch(driver):#driver作为一个形参数传入到封装的函数里面
    #conding = utf-8
    import time
    from selenium.webdriver.common.keys import Keys
    #选择往返地
    time.sleep(3)#只能等待时间
    driver.find_element_by_id("fDepCity").click()
    driver.find_element_by_id("fDepCity").send_keys(u"北京北京")#触发报错场景
    print("触发输入有误的异常")
    time.sleep(2)
    driver.find_element_by_id("fDepCity").clear()
    
    #出发地为空，抛出异常
    time.sleep(5)
    driver.find_element_by_id("fDepCity").clear()
    time.sleep(3)
    driver.find_element_by_class_name("searchFlight").click()
    driver.implicitly_wait(3)
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element_by_class_name("searchFlight").send_keys(Keys.ENTER)
    driver.switch_to.alert.accept()
    print("回车键关闭弹框")

    #出发地和目的地一样
    driver.implicitly_wait(2)
    driver.find_element_by_id("fDepCity").clear()
    driver.find_element_by_id("fDepCity").send_keys(u"广州")
    driver.implicitly_wait(8)
    print("选择出发地")
    driver.find_element_by_id("fArrCity").click()
    driver.find_element_by_id("fArrCity").clear()
    driver.find_element_by_id("fArrCity").send_keys(u"广州")
    time.sleep(3)
    js = "$('input[id=fDepDate]').removeAttr('readonly')" # jQuery，移除属性将日期设置为可以输入的文本框
    driver.execute_script(js)
    date = driver.find_element_by_id('fDepDate')
    date.clear()
    date.send_keys('2019-07-19')
    print("重置出发日期")
    driver.implicitly_wait(3)
    driver.find_element_by_class_name("searchFlight").click()
    print("弹框提示出发地和目的地不能一致")
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element_by_class_name("searchFlight").send_keys(Keys.ENTER)
    driver.switch_to.alert.accept()

    #搜索无航班
    driver.implicitly_wait(2)
    driver.find_element_by_id("fDepCity").send_keys(u"惠州")
    driver.implicitly_wait(8)
    print("选择出发地")
    driver.find_element_by_id("fArrCity").click()
    driver.find_element_by_id("fArrCity").clear()
    time.sleep(4)
    driver.find_element_by_id("fArrCity").send_keys(u"乌鲁木齐")
    time.sleep(6)
    js = "$('input[id=fDepDate]').removeAttr('readonly')" # jQuery，移除属性将日期设置为可以输入的文本框
    driver.execute_script(js)
    date = driver.find_element_by_id('fDepDate')
    date.clear()
    date.send_keys('2019-07-19')
    print("重置出发日期")
    time.sleep(4)
    driver.find_element_by_class_name("searchFlight").click()
    time.sleep(3)
   # titlle = driver.find_element_by_class_name("alertinfo-error")
    time.sleep(3)
    print("不存在惠州到新疆的航班")
    #删除cookie
    time.sleep(3)
    cookie = driver.get_cookies()
    print("打印cookie信息:%s"%cookie)
    driver.delete_all_cookies()#s删除所有的cookie
    print("清除所有的cookie")
    print("等待中...")
    time.sleep(10)
    #关闭浏览器
    driver.quit()

def xunhuan():
    #d导入包
    import time
    from selenium import webdriver
    #打开浏览器输入URL
    driver = webdriver.Chrome()
    url = "https://www.csair.com/cn/index.shtml"
    driver.get(url)#这里的打开浏览器输入URL放在sesrch外面，是要与捕获异常后执行的关闭浏览器的代码对应
    print("访问首页")
    try:
        sesrch(driver)#driver作为实参传入sesrch()函数里
    except BaseException:
        print("异常中断")
        time.sleep(3)
        cookie = driver.get_cookies()
        print("打印cookie信息:%s"%cookie)
        driver.delete_all_cookies()#s删除所有的cookie
        print("清除所有的cookie")
        print("等待中...")
        # print("等待中...")
        # time.sleep(10)
        # #关闭浏览器
        driver.quit()
        xunhuan()
#调用函数


i = 0
while i<500:
    #i = 0
    xunhuan()
    i = i+1  
    print("执行次数%s"%i)
