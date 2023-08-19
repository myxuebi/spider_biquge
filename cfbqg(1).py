import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless=new")
dpath = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=dpath, options=options)

biquge_url = "https://www.beqege.com"

def xiaoshuospider(url):
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    driverc = webdriver.Chrome(service=dpath, options=options)
    driverc.get(url)
    content = driverc.execute_script("return document.documentElement.outerHTML")
    bcontent = BeautifulSoup(content, "html.parser")
    # print(bcontent.findAll(attrs={"id":"content","p":''})[0].text)
    # print(content)
    content = bcontent.findAll(attrs={"id": "content", "p": ''})[0].text
    title = driverc.title
    # print(title)

    driverc.quit()
    return(title,content)

def xiaoshuomulu(url):
    driver.get(url)
    content = driver.execute_script("return document.documentElement.outerHTML")
    # print(content)
    bcontent = BeautifulSoup(content,"html.parser")
    list = bcontent.findAll("dd")
    name = bcontent.findAll("div",id="info")
    print(name[0].text)
    # print(name[0].contents[1].text)
    bookname = name[0].contents[1].text
    f = open(f"{bookname}.txt", "a")
    # print(list)
    for i in list:
        # i = str(i)
        # print(str(i))
        # ii = str(i)
        # print(i.a['href'] + i.text)
        # print(biquge_url+i.a['href'])
        data = xiaoshuospider(biquge_url+i.a['href'])
        print(f"已下载 {data[0]}")
        f.write(data[0])
        f.write(data[1])
        # print(data)

        # time.sleep(60)
        # print("1")


url = input("请输入您要下载小说的目录地址，仅支持 www.beqege.com 里面的小说 \n举个栗子：https://www.beqege.com/67991/ \n请输入图书目录url地址：")
xiaoshuomulu(url)