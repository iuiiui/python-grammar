# ==================== 文件读写常用方法 ====================

# 1. 基本写入文件
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!\n')
    f.write('第二行内容\n')
    f.write('第三行内容\n')
print("写入完成")

# 2. 读取整个文件
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("读取全部内容:")
    print(content)

# 3. 按行读取（返回列表）
with open('test.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print("按行读取:")
    for i, line in enumerate(lines, 1):
        print(f"第{i}行: {line.strip()}")

# 4. 逐行读取（适合大文件，节省内存）
print("\n逐行读取:")
with open('test.txt', 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        print(f"第{line_num}行: {line.strip()}")

# 5. 追加写入
with open('test.txt', 'a', encoding='utf-8') as f:
    f.write('追加的内容\n')
    f.write('再追加一行\n')
print("\n追加完成")

# 6. 读取指定字节数
with open('test.txt', 'r', encoding='utf-8') as f:
    first_10_chars = f.read(10)
    print(f"\n前10个字符: {first_10_chars}")

# 7. 文件指针操作
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f"\n当前指针位置: {f.tell()}")
    f.read(5)
    print(f"读取5个字符后指针位置: {f.tell()}")
    f.seek(0)  # 重置指针到文件开头
    print(f"重置后指针位置: {f.tell()}")

# 8. 写入多行（使用 writelines）
lines_to_write = ['第一行\n', '第二行\n', '第三行\n']
with open('test2.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines_to_write)
print("\nwritelines 写入完成")

# 9. 检查文件是否存在
import os
if os.path.exists('test.txt'):
    print("\n文件存在")
else:
    print("\n文件不存在")

# 10. 获取文件大小
file_size = os.path.getsize('test.txt')
print(f"文件大小: {file_size} 字节")

# 11. 二进制文件读写
# 写入二进制文件
with open('test.bin', 'wb') as f:
    f.write(b'Binary data\x00\x01\x02')

# 读取二进制文件
with open('test.bin', 'rb') as f:
    binary_content = f.read()
    print(f"\n二进制内容: {binary_content}")

# 12. 使用 try-except 处理文件异常
try:
    with open('nonexistent.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("\n文件未找到错误捕获成功")
except PermissionError:
    print("权限错误")
except IOError:
    print("IO错误")

# 13. 同时读写（r+ 模式）
with open('test.txt', 'r+', encoding='utf-8') as f:
    content = f.read()
    print(f"\n原内容长度: {len(content)}")
    f.seek(0)  # 回到文件开头
    f.write('新内容覆盖')  # 会覆盖原有内容

# 14. 创建文件（如果不存在）
with open('new_file.txt', 'w', encoding='utf-8') as f:
    f.write('新创建的文件\n')
print("新文件创建完成")

# 15. 删除文件
# os.remove('test2.txt')
# os.remove('test.bin')
# os.remove('new_file.txt')
# print("文件删除完成")

# ==================== 文件打开模式说明 ====================
# 'r'  - 只读模式（默认），文件必须存在
# 'w'  - 写入模式，会清空文件内容，文件不存在则创建
# 'a'  - 追加模式，在文件末尾添加内容，文件不存在则创建
# 'x'  - 独占创建模式，文件已存在则报错
# 'b'  - 二进制模式（与其他模式组合使用，如 'rb', 'wb'）
# 't'  - 文本模式（默认，可省略）
# '+'  - 更新模式（可读可写，如 'r+', 'w+', 'a+')

print("\n所有文件操作示例完成！")