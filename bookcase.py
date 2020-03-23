bookcase = {'《三国演义》' : '1', '《水浒传》' : '2', '《西游记》' : '3', '《红楼梦》' : '4'}

while True:
    print()
    print('''******功能列表******
    1、查看当前的所有图书列表
    2、查询某本图书的位置
    3、更改图书编号
    4、删除某本图书
    5、增加图书
    0、退出''')

    xz = int(input('请输入你要操作的编号：'))
    if 5>= xz >= 0:
        if xz == 1:
            print('书柜中已有书籍：')
            for bookname in bookcase:
                print(bookname)
        elif xz == 2:
            bookname = input('请输入图书名：')
            if bookname in bookcase:
                print('%s位置：%s' %(bookname, bookcase.get(bookname)))
            else:
                print('%s暂无，不可操作' % bookname)
        elif xz == 3:
            bookname = input('请输入图书名：')
            if bookname in bookcase:
                index = input('请输入要更改的位置：')
                bookcase[bookname] = index
                print('更改成功')
            else:
                print('%s暂无，不可操作' % bookname)
        elif xz == 4:
            bookname = input('请输入图书名称：')
            if bookname in bookcase:
                bookcase.pop(bookname)
                print('%s：删除成功' % bookname)
            else:
                print('%s暂无，不可操作' % bookname)
        elif xz == 5:
            bookname = input('请输入图书名称：')
            if bookname in bookcase:
                print('%s:已存在' % bookname)
            else:
                index = input('请输入图书位置：')
                bookcase[bookname] = index
                print('%s:添加成功' % bookname)
        elif xz == 0:
            break
    else:
        print('操作不合法，请重新输入......')
    b = input('是否继续<y/n>: ')
    if b == 'y':
        break
print('您已离开，欢迎下次体验')