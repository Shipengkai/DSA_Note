def quick_sort(alist, first, last):
    if last <= first:
        return

    mid_value = alist[first]

    i = first
    j = last
    # index

    while i < j:
        # 小 中 大
        while i < j and alist[j] >= mid_value:
            j -= 1
        alist[i] = alist[j]

        while i < j and alist[i] < mid_value:
            i += 1
        alist[j] = alist[i]
    alist[i] = mid_value

    quick_sort(alist, first, i-1)
    quick_sort(alist, i+1, last)


def q_sort(alist):
    quick_sort(alist, 0, len(alist)-1)


if __name__ == "__main__":
    alist = [777, 0, 3, 2, 1, 56, 14, 63545, 134]
    q_sort(alist)
    print(alist)
