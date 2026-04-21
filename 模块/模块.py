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

import time

# ==================== 时间模块常用方法 ====================
# 获取当前时间戳（自1970年1月1日以来的秒数）
print("当前时间戳:", time.time())

# 暂停程序执行（秒）
# time.sleep(1)

# 获取本地时间（结构化时间对象）
local_time = time.localtime()
print("本地时间:", local_time)
print("年:", local_time.tm_year)
print("月:", local_time.tm_mon)
print("日:", local_time.tm_mday)
print("时:", local_time.tm_hour)
print("分:", local_time.tm_min)
print("秒:", local_time.tm_sec)
print("星期:", local_time.tm_wday)  # 0=星期一, 6=星期日
print("一年中的第几天:", local_time.tm_yday)

# 获取UTC时间
utc_time = time.gmtime()
print("UTC时间:", utc_time)

# 将结构化时间转换为时间戳
print("时间戳转换:", time.mktime(local_time))

# 格式化时间输出
print("格式化时间:", time.strftime('%Y-%m-%d %H:%M:%S', local_time))
print("日期格式:", time.strftime('%Y/%m/%d', local_time))
print("时间格式:", time.strftime('%H:%M:%S', local_time))

# 常用格式化符号：
# %Y - 四位年份  %y - 两位年份
# %m - 月份(01-12)  %d - 日期(01-31)
# %H - 小时(00-23)  %I - 小时(01-12)
# %M - 分钟(00-59)  %S - 秒(00-59)
# %A - 完整星期名  %a - 缩写星期名
# %B - 完整月份名  %b - 缩写月份名
# %p - AM/PM

# 将字符串解析为结构化时间
str_time = '2024-01-15 14:30:00'
parsed_time = time.strptime(str_time, '%Y-%m-%d %H:%M:%S')
print("解析时间:", parsed_time)

# 获取可读的时间字符串
print("可读时间:", time.asctime(local_time))
print("当前时间:", time.ctime())

# 性能计时
start = time.perf_counter()
time.sleep(0.1)
end = time.perf_counter()
print(f"耗时: {end - start:.4f} 秒")

# 获取进程时间
print("进程时间:", time.process_time())

# 自定义模块
# 同级模块
# 非同级模块
# import sys
# sys.path.append("../") #把指定目录也变成工作目录