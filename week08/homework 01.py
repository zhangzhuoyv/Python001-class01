# 扁平序列--只能容纳一种数据类型
"""

str , int ,float, 这些都属于 扁平序列

"""

# 非扁平序列如下：

list=[1,2,'hello',3.14]
tuple =(1,2,'hello',3.14)
dict ={'a':1,2:'b',3.14:'hello'}

from collections import deque

d = deque(123,'abc',[456,'jkl'])