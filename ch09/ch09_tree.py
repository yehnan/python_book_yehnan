

tree_a = ['-', 4, 1]
tree_b = ['/', 10, 2]
tree_c = ['+', tree_a, tree_b]
tree_d = ['+', 3, tree_c]
tree_e = ['-', 4, 2]
tree_f = ['*', tree_e, tree_d]

import operator

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.floordiv}
       
def cal(tree):
    if type(tree) == int:
        return tree
    else:
        return ops[tree[0]](cal(tree[1]), cal(tree[2]))

print(cal(tree_f))

