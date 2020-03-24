# list 可变的有序集合，索引从0开始
list = ['dahuang', 'xiaohuang']

# len()函数获取list元素个数
len(list)

# 取最后一个元素 可以用 -1,以此类推，-2 ，-3 等
list[-1]

# 追加元素至末尾
list.append('dahong')
# 将元素添加到指定位置 insert(index, 内容)
list.insert(1, 'dog')
# 删除list末尾的元素
list.pop()
#删除指定位置的元素,用pop(i), i是索引位置
list.pop(0)
# 把某个元素替换成别的元素，可以直接复制给对应的索引位置
list[1] = 1

print(list)
# list里面的元素可以不同
list = ['dog2', 2, True, 1.45]
# list元素也可以是另一个list
s = ['xiaoming', 'xiaoli', ['xiaohuang', 'xiaohong'], 'name']
# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
l = []
len(l)
print(list)

#**************************************

# tuple
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('java', 'php', 'python')
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，
# 但不能赋值成另外的元素。

#**************************************

# dict
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，
# 使用键-值（key-value）存储，具有极快的查找速度。
#举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
classmates = {'java' : 20, 'php' : 20}
#获取value
classmates['java']
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
classmates['java'] = 30

#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
#如果key不存在，dict就会报错：
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：存在True,否则False
'java' in classmates

#*******************************

#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
