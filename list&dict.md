# 操作比较 list and dict
    # 添加
        list: append, extend, insert
        dict: b[k] = v

    # 删除
        list: pop, remove﹡
        dict: pop

    # 反查
        list: index, count
        dict: --

    # 其他
        list：reverse, sort
        dict：has_key, update

# 时间复杂度 list   展示文件：TList.py
    # O(1)
        按索引取值, 赋值: b[i]
        append()
        pop()

    # O(n)
        __add__(+)         #因为复制到新列表，所以是n+k;   list += 'a'自带优化与list = list + ‘a’不同，后者复制了list
        pop(i)
    #注： list的各种method需要保证 索引O(1)



# 所有时间复杂度
    https://wiki.python.org/moin/TimeComplexity