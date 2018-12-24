# 导入相关包

import re

#查找数字
#r表示字符串不转义

p = re.compile(r"\d+")

# 在字符串"one12twothree33456four0098"中进行查找，按照规则指定的规则进行查找
result = p.match("one12twothree33456four0098")
result2 = p.match("one12twothree33456four0098",3,18)
# 返回的结果为None，表示没找到,否则会返回match对象
print(result)

print(result2)

#result2 上述代码说明的问题
#1、match可以输入参数表示起始位置
#2、查找到的结果只包含一个，表示第一次仅从匹配成功的内容

#匹配到的结果
print(result2[0])
#匹配到的数字从哪开始
print(result2.start(0))
#匹配到的数字从哪结束
print(result2.end(0))