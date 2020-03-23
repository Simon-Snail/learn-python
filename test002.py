#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('''English test ......

please enter your name

Sorry, try again

send usage statistics''')

print('------------------')

#输入
name = input("输入：")

#结果输出
if name == "please enter your name":
	print("Correct", name)
elif name == "Sorry, try again": 
	print("Correct", name)
elif name == "send usage statistics":
	print("Correct", name)
else:
	print("error", name)
