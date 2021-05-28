import xml.dom.minidom


dom = xml.dom.minidom.parse("sample1.xml")
# print(dom.toxml())
root = dom.documentElement
# print(help(root))
# 得到树的根节点
root_element = dom.firstChild
print(root_element)
children_element = root_element.childNodes
children_element1 = root_element._get_childNodes()

print(children_element)
print(children_element1)
# for e in children_element:
#     children1_element = e.childNodes
#     print(e)