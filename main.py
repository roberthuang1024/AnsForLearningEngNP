# coding = UTF-8
# 开发者：孤言
# 版本: Alpha 0.0.1
# 开源协议: CC0
# 警告：本工具仅供编程学习交流，因错误理解工具意图而使用本工具造成的一切后果作者概不负责！

import os
import sys
import requests

print("[警告]本工具仅供编程学习交流，因错误理解工具意图而使用本工具造成的一切后果作者概不负责！")

localPath = os.path.dirname(os.path.realpath(sys.argv[0]))+'\\'

# 检查/创建download文件夹
if not os.path.exists(localPath + 'download'):
    os.makedirs(localPath + 'download')

# 读取配置文件
try:
    config = open(localPath+"config.txt", 'r',
                  encoding='UTF-8').read().split('\n')
except FileNotFoundError:
    print("配置文件丢失，请检查！")
    input()
    sys.exit()

indexCode = int(config[0])
keyword = config[1]
addMode = int(config[2])

print("正在查找，请稍等...")

while True:
    # print("提取："+str(indexCode))
    # 提取网页html
    try:
        htmlFile = requests.get('https://www.xyybs.com/index.php?m=wap&a=show&catid=145&id=' +
                                str(indexCode) +
                                '.html')
    except ConnectionError:
        print("网络异常，请稍后再试！")
        input()
        sys.exit()

    htmlFile.encoding = 'utf-8'
    htmlTxt = htmlFile.text

    print(indexCode)

    # 提取网页标题
    try:
        webTitle = htmlTxt[htmlTxt.index('<h3>')+4:
                           htmlTxt.index('</h3>')]
    except ValueError:
        webTitle = 'none'

    if '请在报纸出版日期日之后访问' in htmlTxt:
        print("该报纸答案尚未出版!")
        input()
        sys.exit()

    # 网页标题是否包含关键字
    elif keyword in webTitle:
        print('你想要 "' + webTitle + '" 吗？' +
              ' (ID: ' + str(indexCode) + ')')
        print('【0】下载该答案    【1】寻找下一个    【2】寻找上一个')
        option = int(input())

        if option == 0:
            # 下载答案
            try:
                ansLink = htmlTxt[htmlTxt.index('<p>点击下载')+16:
                                  htmlTxt.index('.docx"')+5]
                ans = requests.get("https:"+ansLink).content

                # 下载文件
                with open(localPath + 'download\\' +
                          webTitle+'.docx', 'wb') as f:
                    f.write(ans)
                print("\n下载成功。")

                # 更新配置文件
                open(localPath+"config.txt", 'w',
                     encoding='UTF-8').write(str(indexCode)+'\n' +
                                             keyword+'\n' +
                                             str(addMode))

                if input("是否继续搜索？【0/1】") == '0':
                    break

            except ValueError:
                print("本页面不含答案！")

        elif option == 1:
            addMode = 1
            print("正在继续查找，请稍等...")

        elif option == 2:
            addMode = -1
            print("正在继续查找，请稍等...")

    indexCode += addMode
