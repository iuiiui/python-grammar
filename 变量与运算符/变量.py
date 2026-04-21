# 获取变量的内存地址
a = 1
address = id(a)
print(address)

# 获取变量的数据类型
int_var = 2
print(type(int_var), int_var)

none_var = None
print(type(none_var), none_var)

# 强制转换数据类型
int_var = 3
str_var = str(int_var)
print(type(str_var), str_var)

# 获取变量的属性
str_var = 'hello'
print(dir(str_var))

# 格式化输入与输出
# str_var = input('请输入：')
print('%s %s' % ('hello', 'world'))
print('{} {}'.format('hello', 'world'))
print(f'{int_var} {str_var}')

# 字符串访问
str_var = 'hello world'
print(str_var[0])
print(str_var[-1])
print(str_var[0:5])
print(str_var[:5])
print(str_var[5:])
print(str_var[::2])
print(str_var[::-1])
print(str_var[::],str_var[:])

# 字符串查找
str_var = 'hello world'
print(str_var.find('l'))

# 字符串切割
str_var = 'hello world'
split_str_var = str_var.split(' ')
print(type(split_str_var), split_str_var)

# 字符串替换
str_var = 'hello world'
print(str_var.replace('hello', 'hi'))

# 字符串包含
str_var = 'hello world'
print('hello' in str_var)