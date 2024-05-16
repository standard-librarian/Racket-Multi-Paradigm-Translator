from functools import reduce
import operator
from math import sqrt
binary_func_all = lambda func: lambda l: reduce(func, l)
add_all = binary_func_all(operator.add) # +
sub_all = binary_func_all(operator.sub) # -
mul_all = binary_func_all(operator.mul) # *
div_all = binary_func_all(operator.truediv) # /

add_all((1, 2, 3))
sub_all((4, 5, 6))
mul_all((2, 5, 7))
div_all((7, 8, 9))
max(3, -2, 4.1, 1/3)

all_binary_func = lambda func: lambda l: all([True if func(l[i -1], l[i]) else False for i in range(1, len(l))])
all_eq = all_binary_func(operator.eq) # ==
all_gt = all_binary_func(operator.gt) # >
all_ge = all_binary_func(operator.ge) # >=
all_lt = all_binary_func(operator.lt) # <
all_le = all_binary_func(operator.le) # <=

all_eq((2, 2))
all_eq((sqrt(4), 3))
all_gt((3, 4))
all_lt((3, 4))
all_ge((2, 2, 3))

print(add_all((1, 2, mul_all((2, 5)))))