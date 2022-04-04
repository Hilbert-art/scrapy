from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions

def main():
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}

    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_experimental_option('w3c', False)
    location = r"F:\All_python_code\scrapy\chrome-win\chrome.exe"
    # 在options里面增加读取位置为主程序位置
    options.binary_location = location

    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome("F:\All_python_code\scrapy\chromedriver.exe", options=options)

    driver.get("http://www.4399dmw.com/donghua/")

    action = TouchActions(driver)
    action.tap_and_hold(75,125).release(75,125)

    time.sleep(10)

    # 关闭webdriver
    driver.quit()


if __name__ == '__main__':
    main()
