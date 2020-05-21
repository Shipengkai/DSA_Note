def dicadd(lis, dic):
    for x in lis:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1


def dicreduce(lis, dic):
    for x in lis:
        if x in dic:
            dic[x] -= 1
        else:
            dic[x] = -1


def anagram_solution(str1, str2):
    lis1, lis2 = list(str1), list(str2)
    dic = {}
    dicadd(lis1, dic)
    dicreduce(lis2, dic)
    for x in dic:
        if dic[x] != 0:
            return False
    return True


s1 = '哈python'
s2 = 'ty哈phon'
print(anagram_solution(s1, s2))
