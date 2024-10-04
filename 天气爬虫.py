# 导入 requests 库，用于发送 HTTP 请求
import requests

# 导入 BeautifulSoup 库，用于解析 HTML 内容
from bs4 import BeautifulSoup

# 目标网站的 URL
url = 'https://www.weather.com.cn/weather1d/101181404.shtml#input'

# 发送 HTTP GET 请求获取网页内容
response = requests.get(url)

# 检查请求是否成功（状态码 200 表示成功）
if response.status_code == 200:
    # 使用 BeautifulSoup 解析 HTML 内容，指定使用 'html.parser' 解析器
    soup = BeautifulSoup(response.content, 'html.parser')

    # 查找网页中包含天气信息的 div 标签，假设其 class 为 'weather-info'
    weather_info1 = soup.find('div', class_='con today clearfix')

    weather_info2 = weather_info1.find('div', class_='left fl')
    weather_info3 = weather_info2.find('div', class_='left-div')
    weather_info4 = weather_info3.find('div', class_='today clearfix',id="today")
    weather_info5 = weather_info4.find('div', class_='t')
    weather_info6 = weather_info5.find('div', class_='sk')
    print(weather_info5.prettify())
    print(weather_info6.prettify())

    temperature = weather_info6.find('span', class_='tem')



    # 打印提取的温度和天气状况信息
    print(f"Temperature: {temperature}")
else:
    # 如果请求失败，打印错误信息
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

