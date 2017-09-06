# __author: TungShine
# __date: 2017/9/6
# __description:


import xml.etree.ElementTree as et

tree = et.parse('xml_test')
root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)  # tag: element元素标签名称 attrib: element元素标签属性名称及值
#     for _child in iter(child):
#         print(_child.tag, _child.attrib)


for country in root.findall('country'):
    print(country.tag, country.attrib)

# tree.write('xml_test.xml')
