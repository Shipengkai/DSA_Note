def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    i = first
    j = last
    while i < j:
        while i < j and alist[j] >= mid_value:
            j -= 1
        alist[i] = alist[j]

        while i < j and alist[i] < mid_value:
            i += 1
        alist[j] = alist[i]
    alist[i] = mid_value
    quick_sort(alist, first, i-1)
    quick_sort(alist, i+1, last)


def bubble_sort(alist):
    n = len(alist)
    for j in range(n-2):
        count = 0
        for i in range(n-j-1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            break


if __name__ == "__main__":
    alist = [1, 2, 3, 4, 5, 3, 2, 1]
    quick_sort(alist, 0, len(alist)-1)
    print(alist)
