#  遞歸 一層一層
# n! = 1*2*3...*(n-1)*n
def nore(n):
    res = 1
    for it in range(1, n + 1):
        res = res * it
    return res


def recursion(n):
    if n == 1:
        return n
    return n * recursion(n-1)


print(nore(4))
print(recursion(4))
