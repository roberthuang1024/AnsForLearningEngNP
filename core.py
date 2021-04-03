# coding = UTF-8
# 开发者：孤言
# 版本: Alpha 0.0.0
# 开源协议: CC0
# 警告：本工具仅供编程学习交流，因错误理解工具意图而使用本工具造成的一切后果作者概不负责！

import requests

print("[警告]本工具仅供编程学习交流，因错误理解工具意图而使用本工具造成的一切后果作者概不负责！")

# 读取配置文件
config = open("config.txt", 'r', encoding='UTF-8').read().split('\n')
indexCode = int(config[0])
keyword = config[1]

addMode = 1

print("正在查找，请稍等...")

while True:
    # print("提取："+str(indexCode))
    # 提取网页html
    htmlFile = requests.get('https://www.xyybs.com/index.php?m=wap&a=show&ewm=1&catid=152&id=' +
                            str(indexCode) +
                            '.html')
    htmlFile.encoding = 'utf-8'
    htmlTxt = htmlFile.text

    # 提取网页标题
    try:
        webTitle = htmlTxt[htmlTxt.index('<h3>')+4:
                           htmlTxt.index('</h3>')]
    except ValueError:
        webTitle = ''

    # 网页标题是否包含关键字
    if keyword in webTitle:
        print('你想要 "'+webTitle+'" 吗？')
        print('【0】下载该答案    【1】寻找下一个    【2】寻找上一个')
        option = int(input())

        if option == 0:
            # 下载答案
            try:
                ansLink = htmlTxt[htmlTxt.index('<p>点击下载')+16:
                                  htmlTxt.index('.docx"')+5]
                ans = requests.get("https:"+ansLink).content

                with open('C:\\Users\\Administrator\\Desktop\\' +
                          webTitle+'.docx',
                          'wb') as f:
                    f.write(ans)

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
