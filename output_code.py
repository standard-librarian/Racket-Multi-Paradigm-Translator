
from functools import reduce
import operator
from math import sqrt
binary_func_all = lambda func: lambda l: reduce(func, l)
add_all = binary_func_all(operator.add) # +
sub_all = binary_func_all(operator.sub) # -
mul_all = binary_func_all(operator.mul) # *
div_all = binary_func_all(operator.truediv) # /

all_binary_func = lambda func: lambda l: all([True if func(l[i -1], l[i]) else False for i in range(1, len(l))])
all_eq = all_binary_func(operator.eq) # ==
all_gt = all_binary_func(operator.gt) # >
all_ge = all_binary_func(operator.ge) # >=
all_lt = all_binary_func(operator.lt) # <
all_le = all_binary_func(operator.le) # <=

average = lambda lst: div_all((functools.reduce(lambda x, y: add_all((x, y)), lst, 0), length, lst))
print(average(list((1, 2, 3))))
