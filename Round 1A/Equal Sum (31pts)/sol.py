def partitionA(a: list, targetSum: int) -> list:
    """
    input: a (DESC)
    output: l
    """

    l = []
    for i in a:
        if i <= targetSum:
            targetSum -= i
            l.append(i)

    return l


# def partitionB(b: list, maxGap: int) -> list:
#     """return l, r, gap and sum(l) < sum(r)"""
#     b.sort()
#     gap = maxGap + 1
#     l = []
#     r = []
#     while gap > maxGap:
#         pass

#     return l, r, gap

# TIME OUT
def partitionB(remaind: list, l: list, r: list, maxGap: int):
    """return l, r, gap  and sum(l) < sum(r)"""
    if len(remaind) == 0:
        ls = sum(l)
        rs = sum(r)
        gap = abs(ls - rs)
        if not (gap & 1) and gap <= maxGap:  # 짝수 & 범위내
            if ls < rs:
                return l, r, gap
            else:
                return r, l, gap
        else:
            return None

    cur = remaind.pop(-1)
    l.append(cur)
    result = partitionB(remaind, l, r, maxGap)
    if result is not None:
        return result
    l.pop(-1)
    r.append(cur)
    result = partitionB(remaind, l, r, maxGap)
    if result is not None:
        return result
    r.pop(-1)
    remaind.append(cur)


for t in range(int(input())):
    # start
    n = int(input())

    # phase 1
    a = list(range(n, 0, -1))
    print(*a)

    # phase 2
    b = list(map(int, input().split()))

    # phase 3
    # l과 r 자체에 의미는 없으므로 불필요한 반복 줄임
    maxGap = sum(a)
    l, r, gap = partitionB(b[:-1], [b[-1]], [], maxGap)
    print(*(l + partitionA(a, (maxGap+gap)//2)))
