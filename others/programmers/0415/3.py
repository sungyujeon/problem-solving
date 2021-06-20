def get_tree_dict(es, _n):
    _tree_dict = {}
    for i in range(_n):
        _tree_dict[i] = []

    for e in es:
        a, b = e
        _tree_dict[a].append(b)
        _tree_dict[b].append(a)

    return _tree_dict
        
def get_parents(treeD, _n, _max_node):
    _parents = [-1] * _n
    visited = [False] * _n
    visited[_max_node] = True

    stack = [_max_node]

    while stack:
        node = stack.pop()
        childs = list(treeD.get(node))

        while childs:
            child = childs.pop()
            if not visited[child]:
                visited[child] = True
                _parents[child] = node
                stack.append(child)
    return _parents

def get_leaves(treeD, _n, _max_node):
    _leaves = []
    for i in range(_n):
        if i != _max_node and len(treeD[i]) == 1:
            _leaves.append(i)
    return _leaves

def make_zero(_a, _parents, _leaves):
    res_total = 0
    while _leaves:
        leaf = _leaves.pop()  # leaf
        
        while _parents[leaf] != -1:
            # child
            child_value = _a[leaf]
            _a[leaf] = 0

            parent = _parents[leaf]
            _a[parent] += child_value
            res_total += abs(child_value)

            # leaf를 parent로
            leaf = parent
    return res_total



a = [0,1,-1]
n = len(a)

max_a = max(a)
min_a = min(a)
max_a = max_a if abs(max_a) > abs(min_a) else min_a
max_node = a.index(max_a)
edges = [[1,0], [1,2]]
parents = [-1] * n

res = 0
total = sum(a)
if total == 0:
    flag = True
    for i in range(n):
        if a[i] != 0:
            flag = False
            break
    if flag:
        res = 0
    else:
        tree_dict = get_tree_dict(edges, n)
        parents = get_parents(tree_dict, n, max_node)
        leaves = get_leaves(tree_dict, n, max_node)
        res = make_zero(a, parents, leaves)
else:
    res = -1

print(res)