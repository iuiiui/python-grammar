import copy
# 浅拷贝
a = [[1,2,3],[4,5,6]]
b = a.copy()
print(id(a),id(b))
print(id(a[0]),id(b[0]))
# 深拷贝
c = copy.deepcopy(a)
print(id(a),id(c))
print(id(a[0]),id(c[0]))