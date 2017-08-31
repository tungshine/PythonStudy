# __author   :   TungShine
# __date     :   2017/8/15

product_list = [
    ('Mac Book', 13000),
    ('Iphone7', 7500),
    ('Samsung', 7000),
    ('Cannon', 13000),
]
cart = []
balance = 1000000

print('欢迎光临')

while True:
    for i, v in enumerate(product_list, 1):
        print(i, '号商品为：', v[0])
    product_no = input('请选择您要的商品编号[退出：q]：')
    if product_no.isdigit():
        product_no = int(product_no)
        print(product_no)
        if 0 < product_no <= len(product_list):
            p_item = product_list[product_no - 1]
            if p_item[1] < balance:
                balance -= p_item[1]
                cart.append(p_item)
                print("您选择的商品是%s" % p_item[0])
        else:
            print("无效的商品编号")
    elif product_no == 'q':
        print('您已购买如下商品')
        for i in cart:
            print(i[0], "￥", i[1])
        print('您还剩%s元钱' % balance)
        break
    else:
        print("invalid input")
