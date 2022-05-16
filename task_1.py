
def array_diff(a, b):
    res = []
    for i in a:
        if i not in b:
            res.append(i)
    return res


print(array_diff([2, 41, 3, 2, 1], [2, 3, 1]))

