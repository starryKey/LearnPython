import xml.etree.ElementTree as ET
stu = ET.Element("Student1")

name = ET.SubElement(stu, "Name")
# name.attrib = {"lang11","en"}
name.text = "Test"

age = ET.SubElement(stu, "Age")
age.text = "18"

ET.dump(stu)




# a = ET.Element("A")
# b = ET.SubElement(a, "B")
# c = ET.SubElement(a, "c")
# d = ET.SubElement(c, "d")
#
# ET.dump(a)



