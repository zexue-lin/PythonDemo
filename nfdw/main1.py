import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# 设置 ChromeDriver 路径   # 替换为你的 ChromeDriver 路径
webdriver_service = Service('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
driver = webdriver.Chrome(service=webdriver_service)



# 加载保存的 localStorage 数据
with open('local_storage.json', 'r', encoding='utf-8') as f:
    local_storage_data = json.load(f)

# 加载保存的 cookies 数据
with open('cookies.json', 'r', encoding='utf-8') as f:
    cookies = json.load(f)

# 打开网页
driver.get('https://zhaopin.csg.cn')
time.sleep(5)

# 加载保存的 sessionStorage 数据
with open('session_storage.json', 'r', encoding='utf-8') as f:
    session_storage_data = json.load(f)

# 设置 sessionStorage 数据
for key, value in session_storage_data.items():
    driver.execute_script(f"window.sessionStorage.setItem('{key}', '{value}');")

# 设置 localStorage 数据
for key, value in local_storage_data.items():
    driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

# 设置 cookies
for cookie in cookies:
    driver.add_cookie(cookie)

# 刷新页面，确保 cookies 和 localStorage 生效
driver.refresh()
time.sleep(2)

# 模拟访问的 URL 模板
base_url = 'https://zhaopin.csg.cn/#/post-list-detail?gobackUrl=%2Fjob-list&postId={}&canback=no'

# 定义需要抓取的 postId 列表
post_ids = [
    "0B15AD1C245E4E0EB9348A0433BFA22E",  # 示例postId，循环时替换
    "1B68E21F67134B8E8BD75877EC2D312A",
    "A2597293CFE14BECB4E1414EE058C80C",
    "428A9C8AE4C346F98E6BA2B1D5C0CB49",
    "9CAFD0A36C0F4B668F969B0A721AC599",
    "CE7923F857634904B75A9AE77333D581",
    "AD14B44CF15B476AB1B0F1742F9BBB1B",
    "4CA5D720FC634946942C7BBA3EB731A8",
    "71E86811139D4BA79BF81EDFE3852DCB",
    "CCF55BF323D54381AAE1FC6E38A00B9B",
    "90FD8FA0427C4DFAB6F9563C7F16E863",
    "5567D7C14ECC49379290A922A0B0757D",
    "0B15AD1C245E4E0EB9348A0433BFA22E",
    "D265BD2F67974240862CF8A4F96F31B2",
    "F4263C6C470A4B20831BFB039E5FD94E",
    "E2CA3BBB122645E3BA47A57487B11355",
    "4430E783A3864AE58E2ABE98E436BD60",
    "46F3EDCDDEC446C6A49E3D0F3510BD43",
    "CE1FD6172AC24BA3BB0C8E852D5AC550",
    "2AE970D925BE4D93B3AF5CF68E0230AE",
    "37883F0E67E949648884FD1B6D87E05C",
    "9C35D4A4E27C4245981EF5DFD74D7E15",
    "E917323758374C4F9DEF3AA82E4EB9D3",
    "D787170BA978428C8B276C6503DE0BDC",
    "5BF68FED36194C78B3DE94121A62763B",
    "D41AB9884B9742ACA451AA32A44C7F68",
    "D9709C4EFDF443FBB0156001B7975DDD",
    "EE99417418094410A0D7A431FF5F4DD7",
    "0612C4117B6342428B57FFB1D276AD54",
    "A938B988450740D9A571119DF155D5FC",
    "1AB4E29158F142D0A018053C74864188",
    "3FC89DD9E80E4EE287B60FA50217B954",
    "AB6DA400E3E943E8B18EECCA2B1FF7B1",
    "518E41E81C534E3196CA2E418609D023",
    "B7D5447B9F794C51827F1E633F8FA6C4",
    "1C9B031FC4464B7AB74AD8C51531E5CF",
    "B8894C7AD3BF4052B933C8EBFAE92378",
    "D590A79149B243ADAAE01500C195A7B0",
    "41D980BDF5344765A652E993727A4E05",
    "6CBDE78605BD4121A1F1A35BE9101F31",
    "75F740B25DBC47EE9B540B57ED71F21D",
    "D0E216F88D804000AA1038AE05FF9ABB",
]

# 设置 localStorage 数据
for key, value in local_storage_data.items():
    driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

# 刷新页面，使 localStorage 数据生效
driver.refresh()
time.sleep(2)

# 存储结果的数据结构
data = []

# 循环遍历每个 postId
for post_id in post_ids:
    try:
        # 使用 Selenium 打开网页
        url = base_url.format(post_id)
        driver.get(url)

        # 强制刷新页面以确保每次加载的内容不同
        driver.refresh()

        # 等待几秒钟，以确保页面完全加载
        time.sleep(3)

        # 抓取页面中 id 为 'app' 的元素，并从中找到 class 为 'leftBox' 的内容
        app_element = driver.find_element(By.ID, 'app')
        left_box_elements = app_element.find_elements(By.CLASS_NAME, 'leftBox')

        if left_box_elements:
            # 抓取第 5 个子元素的内容
            fifth_element = left_box_elements[0].find_elements(By.CLASS_NAME, 'item')[4]
            item_value = fifth_element.find_element(By.CLASS_NAME, 'item-value').text
            print(f"PostId: {post_id}, Data: {item_value}")
            data.append({'PostId': post_id, 'Data': item_value})
        else:
            print(f"PostId: {post_id}, LeftBox not found")
            data.append({'PostId': post_id, 'Data': 'LeftBox not found'})

    except Exception as e:
        print(f"PostId: {post_id}, Error: {str(e)}")
        data.append({'PostId': post_id, 'Data': 'Failed to retrieve data'})

# 把结果导出到 Excel
df = pd.DataFrame(data)
df.to_excel('scraped_data.xlsx', index=False)

# 关闭浏览器
driver.quit()
