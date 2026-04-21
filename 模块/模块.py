# from random import randint
#
# # 随机数
# print(randint(1, 10))

# import random
# # 随机数
# print(random.randint(1, 10))

import os

# ==================== 路径操作 ====================
# 获取当前工作目录
print("当前目录:", os.getcwd())

# 拼接路径（跨平台兼容）
path = os.path.join('folder', 'subfolder', 'file.txt')
print("拼接路径:", path)

# 获取绝对路径
print("绝对路径:", os.path.abspath('.'))

# 获取路径的目录部分
print("目录名:", os.path.dirname('/home/user/file.txt'))

# 获取路径的文件名部分
print("文件名:", os.path.basename('/home/user/file.txt'))

# 分割路径
print("分割路径:", os.path.split('/home/user/file.txt'))

# 分割文件扩展名
print("分割扩展名:", os.path.splitext('file.txt'))

# 判断路径是否存在
print("路径存在:", os.path.exists('.'))

# 判断是否为文件
print("是文件:", os.path.isfile('模块.py'))

# 判断是否为目录
print("是目录:", os.path.isdir('.'))

# 获取文件大小（字节）
print("文件大小:", os.path.getsize('模块.py'))

# ==================== 目录操作 ====================
# 获取当前目录下的所有文件和文件夹
print("目录列表:", os.listdir('.'))

# 创建单级目录
os.makedirs('test/subtest', exist_ok=True)

# 删除目录（只能删除空目录）
os.rmdir('test/subtest')

# 递归创建目录
os.makedirs('test/nested/deep', exist_ok=True)

# 递归删除目录树
import shutil
shutil.rmtree('test')

# 重命名文件或目录
# os.rename('old_name', 'new_name')

# ==================== 文件操作 ====================
# 删除文件
# os.remove('file.txt')

# 执行系统命令
# os.system('ls -l')  # Linux/Mac
# os.system('dir')     # Windows

# 获取环境变量
print("PATH环境变量:", os.environ.get('PATH'))

# 设置环境变量
os.environ['MY_VAR'] = 'test_value'

# 获取操作系统名称
print("操作系统:", os.name)  # nt(Windows), posix(Linux/Mac)

# 获取CPU数量
print("CPU数量:", os.cpu_count())

# ==================== os.path常用方法 ====================
import os.path as op

# 规范化路径
print("规范化路径:", op.normpath('./folder/../file.txt'))

# 获取真实路径（解析符号链接）
print("真实路径:", op.realpath('.'))

# 判断是否为绝对路径
print("是绝对路径:", op.isabs('/home/user'))

# 获取最近访问时间
# print("最后访问:", op.getatime('file.txt'))

# 获取最近修改时间
# print("最后修改:", op.getmtime('file.txt'))

# 获取创建时间（Windows）/ 最后状态改变时间（Unix）
# print("创建时间:", op.getctime('file.txt'))