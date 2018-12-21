# import xml.etree.ElementTree as et
#
# tree = et.parse(r"to_edit.xml")
#
# root = tree.getroot()
#
# for ele in root.iter("Name"):
#     print(ele.text)
#
# for stu in root.iter("Student"):
#     name = stu.find("Name")
#
#     if name != None:
#         name.set("test", name.text * 2)
#
# stu = root.find("Student")
#
# #生成一个新的元素
# e = et.Element("ADDer")
# e.attrib = {"a":"b"}
# e.text = "测试"
#
# stu.append(e)
# # 一定要把修改后的内容写入文件，否则无效
# tree.write("to_edit.xml")


import xml.etree.ElementTree as et



try:
    global tree,root
    tree = et.parse('to_edit.xml')
    root = tree.getroot()
except Exception as exc:
    print("解析xml出异常了:{0}".format(exc))


for e in root.iter('School'):
    print(e.text)


for stu in root.iter('Student'):
    name = stu.find('Name')

    if name != None:
        name.set('test', name.text * 2)

stu = root.find('Student')

#生成一个新的 元素
e = et.Element('ADDer')
e.attrib = {'a':'b'}
e.text = '我加的'

stu.append(e)

# 一定要把修改后的内容写回文件，否则修改无效
tree.write('to_edit.xml')