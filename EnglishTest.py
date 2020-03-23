#单词趣味练习

page1 = {'please enter your name' : '请输入你的名字', 'Sorry, try again.' : '对不起，请重试', 'send usage statistics' : '发送使用统计'}
page2 = {'not defined' : '没有定义的', 'list index out of range' : '列表索引超出范围', 'classmates' : '同学们'}
page3 = {'invalid syntax' : '语法无效', 'kid' : '小子', 'teenager' : '青少年', 'adult' : '成人'}
page4 = {'not installed' : '未安装', 'bookcase' : '书柜', 'exercise book' : '练习簿', 'word' : '单词'}

exerciseBooks = {'山贼' : page1, '黄鼠狼勇士' : page2, '黄鼠狼射手' : page3, '朱雀' : page4}

while True:
    print()
    print('''******功能列表******
    1、查看关卡🔪
    2、进入试炼🔪
    3、关卡管理🔪
    0、溜了溜了💨
    ''')
    i = int(input('你的选择：'))
    if 3 >= i >= 0:
        if i == 1:
            for exerciseBook in exerciseBooks:
                print('关卡内容：%s' % exerciseBook)
        elif i == 2:
            while True:
                print('已有关卡：')
                for page in exerciseBooks:
                    print()
                    print(page)
                    print(exerciseBooks[page])
                    print()
                b = input('是否退出试炼<y/n>: ')
                if b == 'y':
                    break
                page = input('进入：')
                while True:
                    print()
                    if page in exerciseBooks:
                        print('已进入：%s...开始试炼...🔪' % page)
                        word = input('请输入攻击命令：🔪')
                        print()
                        if word in exerciseBooks[page]:
                            print('使用【%s】攻击成功，但【%s】一脸鄙视😒' %(word, page))
                        else:
                            print('使用【%s】攻击失败，并且【%s】打了你一拳' %(word, page))
                    else:
                        print('进入失败')
                    b = input('是否逃跑💨<y/n>: ')
                    if b == 'y':
                        break
        elif i == 0:
            break
    else:
        print('输入不合法，请重新输入')
    b = input('是否退出游戏<y/n>: ')
    if b == 'y':
        break

print('您已离开，欢迎下次体验')
    