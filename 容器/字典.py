# 定义
dict_var = {'name': '张三', 'age': 18, 'sex': '男'}
print(type(dict_var))

# 字典访问
print(dict_var['name'])
print(dict_var.get('name'))
print(dict_var.keys())
print(dict_var.values())
print(type(dict_var.keys()))
print(type(dict_var.values()))
print(dict_var.items())

# 字典转换
list_var = list(dict_var.keys())
print(list_var)

# 字典找符合条件的值
dict_var = {'李白': 100, '王维': 90, '白居易': 80}
# 最大值的key
print(max(dict_var, key=dict_var.get))
print({key: value for key, value in dict_var.items() if value == max(dict_var.values())})
print('李白' in dict_var)

# 字典增加、修改、删除
dict_var['张三'] = 18
dict_var['王维'] = 100
dict_var.update({'白居易': 100})
del dict_var['王维']
dict_var.pop('白居易')
print(dict_var)