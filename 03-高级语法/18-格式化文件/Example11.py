import re

# I 表示忽略大小写
p = re.compile(r"([a-z]+) ([a-z]+)",re.I)

m = p.match("merry christmas")
print(m)

print(m.group(1))
print(m.start(0))
print(m.end(0))

print(m.groups())

# 查找
# - search(str,[,pos[, endpos]])：在字符串中查找匹配，pos和endpos表示起始位置
# findall：查找所有
# finditer：查找，返回一个iter结果

import re

p2 = re.compile(r"\d+")

m2 = p2.search("one12twothree33456four0098")

print(m2.group())

rst = p2.findall("one12twothree33456four0098")
print(rst)
print(type(rst))


# 替换
# sub(rep1,str[,count])
#sub替换的案例


p3 = re.compile(r"(\w+) (\w+)")

s = "hello 123 test 456, 909; merry christmas"

rst2 = p3.sub(r"Hello world", s)

print(rst2)


#匹配中文
# 大部分中文内容表示范围是[u4e00-u9fa5],不包括全角标点

title = u"世界 你好！ hello world"

p3 = re.compile("[\u4e00-\u9fa5]+")

rst3 = p3.findall(title)
print(rst3)


# 贪婪和非贪婪
# - 贪婪：尽可能多的匹配, (*)表示贪婪匹配
# - 非贪婪：找到符合条件的最小内容即可, (?)表示非贪婪
# - 正则默认使用贪婪匹配


testStr = u"<div>name</div><div>age</div>"
# 贪婪
testp1 = re.compile(r"<div>.*</div>")
#非贪婪
testp2 = re.compile(r"<div>.*?</div>")

testm3 = testp1.search(testStr)
print(testm3.group())

testm4 = testp2.search(testStr)
print(testm4.group())


