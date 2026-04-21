# 定义
def func_name(param1, param2):
    # 逻辑
    result = param1 + param2
    return result
# 调用
print(func_name(1, 2))

# 变量可变性与不可变性
# int_var = 1
# print(id(int_var))
# int_var = 2
# print(id(int_var))
# list_var = [1, 2, 3]
# print(id(list_var))
# list_var.append(4)
# print(id(list_var))

# 函数参数传递可变性与不可变性
# def func_int(param1):
#     param1 = 2
#     print(param1)
#
# int_var = 1
# func_int(int_var)
# print(int_var)
# def func_list(param1):
#     param1.append(4)
#     print(param1)
#
# list_var = [1, 2, 3]
# func_list(list_var)
# print(list_var)

# 函数参数
# 默认参数
def func_name(param1, param2=0):
    print(param1, param2)

func_name(1)
# 可变参数
def func_name(*args):
    print(args)

func_name(1, 2, 3)
# 关键字参数
def func_name(**kwargs):
    print(kwargs)
    print(kwargs['name'])

func_name(name='张三', age=18)
# 匿名函数
# 1
func_name = lambda param1, param2: param1 + param2
print(func_name(1, 2))
# 2
print((lambda param1, param2: param1 + param2)(1, 2))
# 3
print(sorted([1, 4, 2, 3], key=lambda x: x))
# 4
print(sorted([{'name': '张三', 'age': 18}, {'name': '李四', 'age': 19}], key=lambda x: x['age']))
# 5
def func_name(param1, param2):
    return lambda x: param1 + param2 + x
print(func_name(1, 2)(3))