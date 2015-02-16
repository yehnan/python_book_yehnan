

tree_a = ['-', 6, 2]
tree_b = ['/', 10, 2]
tree_c = ['+', 3, tree_a, tree_b]
tree_d = ['-', 5, 2, 1]
tree_e = ['*', tree_d, tree_c]

import operator

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.floordiv}
 
def cal_tree(tree):
    if type(tree) == int:
        return tree
    else:
        return cal_forest(tree[1:], tree[0])

def cal_forest(forest, op):
    if len(forest) == 2:
        return ops[op](cal_tree(forest[0]), cal_tree(forest[1]))
    else:
        hsr = cal_forest(forest[:-1], op)
        return ops[op](hsr, cal_tree(forest[-1]))
        
print(cal_tree(tree_e))

