import requests
import json
import os

idlist = [] #这里填上str形式的每一章漫画对应的chapter_id

def get_image_path(chapter_id):
    chapter_url = "https://www.u17.com/comic/ajax.php?mod=chapter&act=get_chapter_v5&chapter_id=" + chapter_id
    conn = requests.session()
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.25"
    }
    conn.cookies.set("U17SID", "", path='/', domain="u17.com") #从cookie中找到自己的U17SID，作为第二个参数
    r = conn.get(chapter_url, headers=headers)
    info = json.loads(r.text)
    chapter_name = info["chapter"]['name']
    if not os.path.exists(chapter_name):
        os.mkdir(chapter_name)
    cnt = 1
    print("当前下载:" + chapter_name)
    for image_info in info["image_list"]:
        file_name = chapter_name + "//" + cnt.__str__() + ".jpg"
        img = requests.get(image_info['src']).content
        with open(file_name, 'wb') as f:
            f.write(img)
        print("第" + cnt.__str__() + "页下载完成")
        cnt += 1

if __name__ == "__main__":
    cnt = 1
    for id in idlist:
        print("开始下载第" + cnt.__str__() + "章节")
        get_image_path(id)
        cnt += 1
