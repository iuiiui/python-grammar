import random
# 替换
str_var = 'hello world'
print(str_var.replace('hello', 'hi'))

# 最大小值
int_var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(int_var), min(int_var))

# 添加、插入、删除
int_var.append(11)
int_var.insert(0, 0)
int_var.pop()
int_var.remove(1)
del int_var[0]
print(int_var)

# 打乱、排序
random.shuffle(int_var)
print(int_var)
int_var.sort()
print(int_var)

# 长度
print(len(int_var))

# 次数
print(int_var.count(0))