
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

sum_ = lambda x, y: add_all((x, y))
x = sum_(1, 2)
print(('it is 10\\n' if all_eq((x, 10)) else 'it is not 10\\n'))
all_gt((1, 2, all_lt((3, 4, all_eq((5, add_all((4, all_ge((3, 4, all_le((99, -0.34)))))))), 6, 7))))
list(map(lambda x: [x] * x, range(20)))
#sum_ = lambda x, y: add_all((x, y))
#x = sum_(1, 2)
#print(('it is 10\\n' if all_eq((x, 10)) else 'it is not 10\\n'))
#all_gt((1, 2, all_lt((3, 4, all_eq((5, add_all((4, all_ge((3, 4, all_le((99, sub_all((0.34)))))))))), 6, 7))))
