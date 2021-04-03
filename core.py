# 开发者：孤言
# 版本: beta 0.0.0
# 警告：本工具仅供编程学习交流，因错误理解工具意图而使用本工具造成的一切后果作者概不负责！

import requests

print("[警告]本工具仅供编程学习交流，因错误理解工具意图而使用本工具造成的一切后果作者概不负责！")

#以只读方式打开temp
temp_file=open("temp",'r')



res = requests.get('https://www.cnblogs.com/easyidea/p/10214559.html')
res.encoding = 'utf-8'