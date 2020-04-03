#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pojo import Student
# print('中文测试正常')
#name = input("please enter you name: ")
#print("Hello, ", name)
# print("100+200+300=",100+200+300)
# classmates = ['java', 'php', 'python']
# n = 2
# r = []
# for i in range(n):
#     r.append(classmates[i])
# print(r)

# print(classmates[-2:])

# l = list(range(100))
# print(l[:])
# import random

# Wuhegu = {'taotie' : '饕餮', 'gonggong' : '共工', 'kuafu' : '夸父'}
# a= random.choice(list(Wuhegu.keys()))
# print(a)
# print([x*x for x in range(11)])
# print([m + n + x for m in 'ABC' for n in 'DEF' for x in 'XYZ'])
# import os
# l = os.listdir('.')
# print(l)
# 导入turtle包的所有内容:
# import os
# print([x*x for x in range(1,10) if x%2 == 0])

# l = [x + n for x in 'ABC' for n in 'CDF']
# print(l)
# print([d for d in os.listdir()])
# L = ['Hello', 'World', 18, 'Apple', None]
# g = (x.lower() for x in L if isinstance(x, str))
# print(next(g))
# from datetime import datetime
# now = datetime.now()
# print(now)


def add(x, y, f):
    return f(x) + f(y)


L1 = ['adam', 'LISA', 'barT']


def normalize(name):
    return name.title()


python = 'python'
#####    输出   #####
words = ['python', 'java', 'c']
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

i = 5
i = 6
def f(arg=i):
    print(arg)


f()

from collections import deque
t = 12345, 54321, 'hello!'
a, b, c = t
print(a, b, c)

