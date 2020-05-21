def bubble(lis):
    if len(lis) < 2:
        return 0
    n = len(lis)
    for j in range(n-1):
        count = 0
        for i in range(n-j-1):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]
                count += 1
        if count == 0:
            break


lis = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]
bubble(lis)
print(lis)
