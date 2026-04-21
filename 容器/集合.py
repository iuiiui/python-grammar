# 定义
set_var = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(set_var))

# 集合不重复、访问、添加、删除
set_var.add(10)
print(len(set_var))
set_var.add(11)
print(11 in set_var)
set_var.remove(11)
print(11 not in set_var)
print(len(set_var))
set_var.clear()
del set_var

# 交集、并集、差集、子集
set_var = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_var1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(set_var.intersection(set_var1))
print(set_var.union(set_var1))
print(set_var1.difference(set_var))
print(set_var.issubset(set_var1))