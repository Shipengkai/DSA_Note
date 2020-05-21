def shell_sort(alist):
    # 希尔排序
    n = len(alist)
    gap = n//2
    while gap != 0:
        for j in range(gap, n):
            i = j
            while i >= gap:
                # i是插入排序插入元素的index
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                else:
                    break
                i -= gap
        print(f"gap: {gap} finished", alist)
        gap //= 2


if __name__ == "__main__":
    lis = [9, 3, 4, 1, 6, 2, 7, 0, 256, 257, 234]
    shell_sort(lis)
    print(lis)
