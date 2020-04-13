

import locale
import os
# file_read('/Users/liujin/Downloads/81f8a509gy1fnjdvkkwgoj20zk0m8ak8.jpg')
f = open('/Users/liujin/settings.xml')
# with open('/Users/liujin/settings.xml') as f:
#     print(f.readline(), end = '')

# for line in f.read():
#     print(line.strip()) 

while True:
    if f.readline() == '':
        break
    else:
        print(f.read().strip())
print(os.uname())
        