# 闭包：内部函数引用了外部函数的变量，即使外部函数执行完毕，内部函数仍然可以访问这些变量

# 1. 基本闭包示例
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))  # 输出: 15
print(closure(20))  # 输出: 30

# 2. 计数器闭包
def create_counter():
    count = [0]  # 使用列表来存储可变状态
    
    def counter():
        count[0] += 1
        return count[0]
    
    return counter

counter1 = create_counter()
print(counter1())  # 输出: 1
print(counter1())  # 输出: 2
print(counter1())  # 输出: 3

counter2 = create_counter()
print(counter2())  # 输出: 1 (独立的计数器)

# 3. 使用 nonlocal 关键字（Python 3）
def create_counter_v2():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter_v2 = create_counter_v2()
print(counter_v2())  # 输出: 1
print(counter_v2())  # 输出: 2
print(counter_v2())  # 输出: 3

# 4. 装饰器（闭包的典型应用）
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数执行完毕")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("张三")

# 5. 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"第 {i + 1} 次执行:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi, {name}!")

greet("李四")

# 6. 闭包保存配置信息
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 输出: 10
print(triple(5))  # 输出: 15

# 7. 查看闭包保存的变量
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(10)
print(closure.__closure__)  # 显示闭包单元
print(closure.__closure__[0].cell_contents)  # 输出: 10
