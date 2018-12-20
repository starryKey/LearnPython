import xml.dom.minidom
# # 负责解析xml文件

from xml.dom.minidom import parse

#使用minidom打开xml文件
DOMTree = xml.dom.minidom.parse("Example02.xml")

#得到文件对象
doc = DOMTree.documentElement

# 显示子元素

for ele in doc.childNodes:
    if ele.nodeName == "Teacher":
        print("---------Node:{0}----------".format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == "Name":
                print("-------Name{0}------".format(child.childNodes[0].data))

            if child.nodeName == "Mobile":
                print("-------Mobile{0}------".format(child.childNodes[0].data))

            if child.nodeName == "Age":
                print("-------Age {0}------".format(child.childNodes[0].data))
                if child.hasAttribute("Detail"):
                    print("Age-Detail:{0}".format(child.getAttribute("Detail")))

