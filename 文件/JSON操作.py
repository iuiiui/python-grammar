# JSON操作
import json

# ==================== 1. 基本JSON序列化与反序列化 ====================
print("=" * 50)
print("1. 基本JSON序列化与反序列化")
print("=" * 50)

# Python对象转JSON字符串(序列化)
data = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "hobbies": ["阅读", "游泳", "编程"]
}

json_str = json.dumps(data, ensure_ascii=False, indent=4)
print("Python对象转JSON字符串:")
print(json_str)

# JSON字符串转Python对象(反序列化)
parsed_data = json.loads(json_str)
print(f"\n解析后的数据: {parsed_data}")
print(f"姓名: {parsed_data['name']}, 年龄: {parsed_data['age']}")

# ==================== 2. JSON文件读写 ====================
print("\n" + "=" * 50)
print("2. JSON文件读写")
print("=" * 50)

# 写入JSON文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("数据已写入 data.json")

# 读取JSON文件
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
print(f"从文件读取的数据: {loaded_data}")

# ==================== 3. 格式化选项 ====================
print("\n" + "=" * 50)
print("3. 格式化选项")
print("=" * 50)

# 紧凑格式(无空格)
compact_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
print(f"紧凑格式: {compact_json}")

# 排序键
sorted_json = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2)
print(f"\n排序键:\n{sorted_json}")

# ==================== 4. 处理复杂数据类型 ====================
print("\n" + "=" * 50)
print("4. 处理复杂数据类型")
print("=" * 50)

from datetime import datetime

complex_data = {
    "timestamp": datetime.now(),
    "value": 3.14159,
    "is_valid": True,
    "null_value": None,
    "nested": {
        "level1": {
            "level2": "deep value"
        }
    }
}

# 自定义编码器处理特殊类型
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return super().default(obj)

custom_json = json.dumps(complex_data, cls=CustomEncoder, ensure_ascii=False, indent=2)
print(f"处理复杂类型:\n{custom_json}")

# ==================== 5. JSON解析错误处理 ====================
print("\n" + "=" * 50)
print("5. JSON解析错误处理")
print("=" * 50)

invalid_json = '{"name": "张三", age: 25}'  # 无效的JSON

try:
    result = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSON解析错误: {e}")
    print(f"错误位置: 行 {e.lineno}, 列 {e.colno}")

# ==================== 6. JSON数据操作 ====================
print("\n" + "=" * 50)
print("6. JSON数据操作")
print("=" * 50)

users_json = '''
[
    {"id": 1, "name": "张三", "age": 25},
    {"id": 2, "name": "李四", "age": 30},
    {"id": 3, "name": "王五", "age": 28}
]
'''

users = json.loads(users_json)

# 查询数据
print("所有用户:")
for user in users:
    print(f"  ID: {user['id']}, 姓名: {user['name']}, 年龄: {user['age']}")

# 过滤数据
adults = [u for u in users if u['age'] >= 28]
print(f"\n年龄>=28的用户: {adults}")

# 添加数据
new_user = {"id": 4, "name": "赵六", "age": 35}
users.append(new_user)
print(f"\n添加新用户后的总数: {len(users)}")

# 删除数据
users.pop(0)  # 删除第一个用户
print(f"删除第一个用户后剩余: {len(users)} 个用户")

# ==================== 7. JSON与字典的转换技巧 ====================
print("\n" + "=" * 50)
print("7. JSON与字典的转换技巧")
print("=" * 50)

# 嵌套字典转JSON
nested_dict = {
    "company": "科技公司",
    "departments": [
        {
            "name": "技术部",
            "employees": [
                {"name": "张三", "position": "工程师"},
                {"name": "李四", "position": "经理"}
            ]
        },
        {
            "name": "市场部",
            "employees": [
                {"name": "王五", "position": "专员"}
            ]
        }
    ]
}

nested_json = json.dumps(nested_dict, ensure_ascii=False, indent=2)
print("嵌套结构JSON:")
print(nested_json)

# 访问嵌套数据
tech_dept = nested_dict['departments'][0]
print(f"\n技术部员工数: {len(tech_dept['employees'])}")

# ==================== 8. 实用工具函数 ====================
print("\n" + "=" * 50)
print("8. 实用工具函数")
print("=" * 50)

def save_json(data, filename):
    """保存数据到JSON文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"数据已保存到 {filename}")

def load_json(filename):
    """从JSON文件加载数据"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return None
    except json.JSONDecodeError:
        print(f"文件 {filename} 不是有效的JSON格式")
        return None

# 使用工具函数
save_json(data, 'example.json')
loaded = load_json('example.json')
if loaded:
    print(f"加载的数据: {loaded}")

# 清理示例文件
import os
if os.path.exists('data.json'):
    os.remove('data.json')
if os.path.exists('example.json'):
    os.remove('example.json')

print("\n示例文件已清理")