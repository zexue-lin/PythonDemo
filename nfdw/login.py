from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import time

# 设置 ChromeDriver 的路径
webdriver_service = Service('C:/Program Files/Google/Chrome/Application/chromedriver.exe')  # 更新为正确的路径
driver = webdriver.Chrome(service=webdriver_service)

# 打开登录页面
driver.get('https://zhaopin.csg.cn')

# 等待手动登录
print("请手动登录并在登录后按 Enter...")
input("登录完成后按 Enter 继续...")

# 获取登录后的 sessionStorage 数据
session_storage_data = driver.execute_script("""
    var storage = {};
    for (var i = 0; i < window.sessionStorage.length; i++) {
        var key = window.sessionStorage.key(i);
        storage[key] = window.sessionStorage.getItem(key);
    }
    return storage;
""")

# 获取登录后的 localStorage 数据
local_storage_data = driver.execute_script("""
    var storage = {};
    for (var i = 0; i < window.localStorage.length; i++) {
        var key = window.localStorage.key(i);
        storage[key] = window.localStorage.getItem(key);
    }
    return storage;
""")

# 获取 cookies 数据
cookies = driver.get_cookies()

# 保存 sessionStorage 数据到文件
with open('session_storage.json', 'w', encoding='utf-8') as f:
    json.dump(session_storage_data, f, ensure_ascii=False, indent=4)

# 保存 localStorage 数据到文件
with open('local_storage.json', 'w', encoding='utf-8') as f:
    json.dump(local_storage_data, f, ensure_ascii=False, indent=4)

# 保存 cookies 数据到文件
with open('cookies.json', 'w', encoding='utf-8') as f:
    json.dump(cookies, f, ensure_ascii=False, indent=4)

print("localStorage SessionStorage 和 cookies 数据已保存。")

# 关闭浏览器
driver.quit()
