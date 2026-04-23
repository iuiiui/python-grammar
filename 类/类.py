# 类：面向对象编程的核心，用于封装数据和行为

# 1. 基本类的定义
class Person:
    # 构造方法（初始化方法）
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age
    
    # 实例方法
    def say_hello(self):
        print(f"Hello, 我叫{self.name}，今年{self.age}岁")

# 创建对象
person = Person("张三", 18)
person.say_hello()  # 输出: Hello, 我叫张三，今年18岁

# 2. 类属性和实例属性
class Student:
    school = "清华大学"  # 类属性（所有实例共享）
    
    def __init__(self, name, score):
        self.name = name   # 实例属性（每个实例独立）
        self.score = score

stu1 = Student("李四", 90)
stu2 = Student("王五", 85)
print(stu1.school)  # 输出: 清华大学
print(stu2.school)  # 输出: 清华大学
Student.school = "北京大学"  # 修改类属性
print(stu1.school)  # 输出: 北京大学

# 3. 私有属性和方法（使用双下划线）
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # 私有属性
    
    def __get_balance(self):  # 私有方法
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存入{amount}元，余额:{self.__balance}元")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"取出{amount}元，余额:{self.__balance}元")
        else:
            print("余额不足或金额无效")

account = BankAccount("张三", 1000)
account.deposit(500)
account.withdraw(200)
# print(account.__balance)  # ❌ AttributeError: 无法直接访问私有属性

# 4. 继承
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name}发出声音")

class Dog(Animal):  # 继承Animal
    def speak(self):  # 重写父类方法
        print(f"{self.name}汪汪叫")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}喵喵叫")

dog = Dog("旺财")
cat = Cat("咪咪")
dog.speak()  # 输出: 旺财汪汪叫
cat.speak()  # 输出: 咪咪喵喵叫

# 5. super() 调用父类方法
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)  # 调用父类的__init__
        self.can_fly = can_fly
    
    def speak(self):
        super().speak()  # 调用父类的speak
        print(f"{self.name}会飞: {self.can_fly}")

bird = Bird("麻雀", True)
bird.speak()

# 6. 多重继承
class Flyable:
    def fly(self):
        print("我会飞")

class Swimmable:
    def swim(self):
        print("我会游泳")

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly()   # 输出: 我会飞
duck.swim()  # 输出: 我会游泳

# 7. 魔法方法（特殊方法）
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):  # 字符串表示
        return f"《{self.title}》 by {self.author}"
    
    def __repr__(self):  # 官方字符串表示
        return f"Book('{self.title}', '{self.author}', {self.price})"
    
    def __eq__(self, other):  # == 运算符
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):  # < 运算符
        return self.price < other.price
    
    def __len__(self):  # len() 函数
        return len(self.title)

book1 = Book("Python编程", "张三", 59.9)
book2 = Book("Python编程", "张三", 59.9)
print(book1)           # 输出: 《Python编程》 by 张三
print(repr(book1))     # 输出: Book('Python编程', '张三', 59.9)
print(book1 == book2)  # 输出: True
print(len(book1))      # 输出: 6

# 8. @property 装饰器（getter/setter）
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        """计算面积（只读属性）"""
        return 3.14159 * self.radius ** 2
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

circle = Circle(5)
print(circle.area)     # 输出: 78.53975
circle.radius = 10
print(circle.area)     # 输出: 314.159
# circle.radius = -1   # ❌ ValueError

# 9. 类方法和静态方法
class MathUtils:
    PI = 3.14159
    
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def from_string(cls, string):
        """类方法：从字符串创建对象"""
        return cls(float(string))
    
    @staticmethod
    def add(a, b):
        """静态方法：不需要访问实例或类"""
        return a + b
    
    def double(self):
        """实例方法"""
        return self.value * 2

obj = MathUtils.from_string("10")
print(obj.double())           # 输出: 20.0
print(MathUtils.add(5, 3))    # 输出: 8

# 10. 抽象基类（接口）
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(f"面积: {rect.area()}")         # 输出: 面积: 50
print(f"周长: {rect.perimeter()}")    # 输出: 周长: 30
# shape = Shape()  # ❌ TypeError: 不能实例化抽象类
