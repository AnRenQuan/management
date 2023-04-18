#1. 用urllib模块，模拟一个浏览器
from urllib.request import urlopen
#2. 输入百度的网址，打开百度
resp = urlopen("http://www.baidu.com")
#3. 打印抓取到的内容
   #print(resp.read().decode("utf-8"))
#4. 创建文件
with open("mybaidu.html",mode="w",encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8")) #5. 把抓取到的内容写入文件中