#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'单词趣味练习单机版🎮'

__author__ = 'Simon'

import random

# 妖界👹
page1 = {'please enter your name': '请输入你的名字',
         'Sorry, try again.': '对不起，请重试', 'send usage statistics': '发送使用统计'}
page2 = {'not defined': '没有定义的',
         'list index out of range': '列表索引超出范围', 'classmates': '同学们'}
page3 = {'invalid syntax': '语法无效', 'kid': '小子',
         'teenager': '青少年', 'adult': '成人', 'baby': '宝宝', 'Aunt': '阿姨'}
page4 = {'not installed': '未安装', 'bookcase': '书柜',
         'exercise book': '练习簿', 'word': '单词'}
page5 = {'function': '函数，功能', 'collection': '集合',
         'power': '功率，力量，幂', 'array': '数组', 'synchronized': '同步'}
page6 = {'WeChat': '微信', 'pay': '支付', 'favorites': 'n. 收藏夹',
         'My Posts': '我的帖子', 'settings': '设置', 'health': 'n. 健康；卫生；保健；兴旺', 'check': '检查', 'heartbeat': '心跳'}
page7 = {'moment': 'n. 重要，契机；瞬间；重要时刻；指定时刻', 'moments': 'n. 片刻（moment复数形式）--朋友圈',
         'scan': 'vt. 扫描；浏览；细看；详细调查；标出格律 vi. 扫描；扫掠 n. 扫描；浏览；审视；细看 --扫一扫',
         'shake': '摇动', 'search': '搜索', 'tag': '标签', 'me': '我', 'chat': '闲谈，聊天, 聊天室',
         'contact': '联系', 'contacts': '联系人', 'discover': '发现'}

# Animal
# watch
page8 = {'Elastic Compute Service': '弹性计算服务简称：云服务器ECS'}

page9 = {'this is the first comment': '这是第一条评论', 'floor division': '向下取整',
         'immutable': '不可变', 'A simple example class': '一个简单的示例类', 'A simple example': '一个简单的例子'}

page10 = {'retries': '重试', 'reminder': '提醒', 'prompt': '提示'}

sequence = {'list': '列表，清单，明细表', 'tuple': '元组',
            'range': '范围', 'sequence': '序列'}

# 地区🔪
Jiuwulin = {'山贼': page1, '黄鼠狼勇士': page2, '黄鼠狼射手': page3,
            '朱雀': page4, '村民': page5, '流浪武士': page6, '鸣蛇': page7}
Changyangshan = {}
Tianshan = {}
Sishui = {}
Liulihuanjing = {}
Shentu = {}

Jiuli = {'酒乌林': 'Jiuwulin'}

weixin = {}
qq = {}

game = {}

while True:
    print()
    print('''******游戏首页******
    1、查看关卡🔪
    2、进入试炼🔪
    3、关卡管理🔪
    0、溜了溜了💨
    ''')
    i = int(input('【你的选择】：'))
    if 3 >= i >= 0:
        if i == 1:
            for k, v in Jiuwulin.items():
                print()
                print(f'【关卡内容】：{k}')
                print(f'【攻击招式】：{v}')
        elif i == 2:
            while True:
                print('【已有关卡】')
                for k, v in Jiuwulin.items():
                    print()
                    print(k)
                    print(v)
                print()
                b = input('是否退出试炼<y/n>: ')
                if b == 'y':
                    break
                print()
                page = input('【进入】：')
                errorSum = 0
                while True:
                    print()
                    if page in Jiuwulin:
                        print(f'已进入：{page}...开始试炼...🔪')
                        key = random.choice(list(Jiuwulin[page].keys()))
                        value = Jiuwulin[page][key]
                        print(f'{page}先你一步，向你抛出了终极问题【{value}】，你可以用对等的攻击抵消...')
                        word = input('请输入攻击命令：🔪')
                        print()
                        if word == key:
                            print(f'使用【{word}】抵消成功，但【{page}】一脸鄙视😒')
                        else:
                            errorSum = errorSum + 1
                            print(f'使用【{word}】抵消失败，并且【{page}】打了你一拳👊')
                            if errorSum == 3:
                                errorSum = 0
                                print(f'【{page}】想你发出了嘲讽👎：太菜了......嘀嘀咕咕')
                    else:
                        print('进入失败')
                    b = input('是否逃跑💨<y/n>: ')
                    if b == 'y':
                        break
        elif i == 3:
            pass
        elif i == 0:
            break
    else:
        print('输入不合法，请重新输入')
    b = input('是否退出游戏<y/n>: ')
    if b == 'y':
        break

print('您已离开，欢迎下次体验')
