import xml.etree.ElementTree as ET
# stu = et.Element("Student1")
#
# name = et.SubElement(stu, "Name")
# name.attrib = {"lang11","en"}
# name.text = "Test"
#
# age = et.SubElement(stu, "Age")
# age.text = 18
#
# et.dump(stu)
#
#


a = ET.Element("A")
b = ET.SubElement(a, "B")
c = ET.SubElement(a, "c")
d = ET.SubElement(c, "d")

ET.dump(a)



