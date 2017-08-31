# __author   :   TungShine
# __date     :   2017/8/17
# 文件操作
f = open("测试", "r", encoding="utf-8")
data = f.readlines()  # 将读取文件类容独立出来，优化读取文件效率
f.close()

for i, v in enumerate(data):
    # num += 1
    if i == 2:
        v = ''.join((v.strip(), 'good'))
    print(v.strip())


# for i in f:  # 内部做成一个迭代器，用一行去一行
#     print(i.strip())

# with open('测试', 'r', encoding='utf-8') as f_read, open('测试2', 'w', encoding='utf-8') as f_write:
#     for line in f_read:
#         f_write.write(line)
