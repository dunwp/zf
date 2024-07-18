import requests as req;
import re   # 正则表达式,必须会用
# import threading # 多线程

headres = {
    'User-Agent ':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.188'
}
url = "https://www.win4000.com/wallpaper_detail_41291.html"

s= req.get(url, headers=headres)
name = re.findall(r'<h3 class="tit">(.*?)<\/h3>', s.text)
img_url = re.findall(r'<img src=".*?" data-src="(.*?)" alt= '' ', s.text)
print(name)
""" 
for new_name, new_img  in zip(name, img_url):
    with open(new_name + ".jpg", 'wb')as f:     
        print("正在保存..." + new_name)
        # f.write(b)将字节数据b写入到二进制文件f,返回是实际写入的字节数
        f.write(req.get{new_img, headers=headres}.content)  
 """
