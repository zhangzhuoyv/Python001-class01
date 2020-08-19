# 自定义函数，实现map 功能

def diy_map(func, *iterables): # *iterables  ([1,2,3],[4,5,6],[7,8,9])  传入的多个可迭代对象，封装程元素

    for args in zip(*iterables):
# zip(*iterables) 就是对 iterables拆包，相当于与 zip([1,2,3],[4,5,6],[7,8,9]) ---- （1，4，7），（2，5，8），（3，6，9）
#所以 args  分别接收了三个 元素 （1，4，7），（2，5，8），（3，6，9）


        yield func(*args) # 全部逐个给函数


def add(*x):  # *arg 对应 *x
    return sum(x)

a_list=[1,2,3]
b_list=[4,5,6]
c_list=[7,8,9]


#加法函数验证
foo =diy_map(add,a_list,b_list,c_list)
print(list(foo))


foo2=map(add,a_list,b_list,c_list)
print(list(foo2))


#匿名函数验证
foo3 = diy_map(lambda x,y:x+y ,a_list,b_list)
print(list(foo3))

foo4 = map(lambda x,y:x+y ,a_list,b_list)
print(list(foo4))




