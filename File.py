


# file_read('/Users/liujin/Downloads/81f8a509gy1fnjdvkkwgoj20zk0m8ak8.jpg')

with open('/Users/liujin/settings.xml') as f:
    for line in f:
        print(line, end = '')

print(f.closed)