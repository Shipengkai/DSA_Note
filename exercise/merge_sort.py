def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])
    lis = []
    i, j = 0, 0
    while i < mid and j < n-mid:
        if left_list[i] <= right_list[j]:
            lis.append(left_list[i])
            i += 1
        else:
            lis.append(right_list[j])
            j += 1
    lis += left_list[i:]
    lis += right_list[j:]
    return lis


if __name__ == "__main__":
    lis = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]
    lis = merge_sort(lis)
    print(lis)
