def co_val(set1,set2):
    inter_set = set1.intersection(set2)
    inter_list = list(inter_set)
    inter_list.sort()
    keep_val = []
    if len(inter_list) == 0:
        print(0)
        return 0
    less = inter_list[0]
    most = inter_list[len(inter_list)-1]
    for i in range(less,most+1):
        i = str(i)
        res = 0
        for digi in i:
            digi = int(digi)
            res += digi
        if res%2 != 0:
            keep_val.append(res)
    keep_val = tuple(keep_val)
    print(sum(keep_val))
    return sum(keep_val)

co_val({19,22,5,7,8},{1,2,19,22,20})
co_val({1,2,3,4},{5,6,7,8})
co_val({11,12,16},{13,14,15,16})
co_val({11,12,24,16},{13,14,15,16,24})