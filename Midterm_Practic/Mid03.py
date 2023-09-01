def sum_time (*time):
    hr = 0
    min = 0
    sec =0
    #print(time)
    for ti in time:
        pass
    #print(ti)
    for times in ti:
        timess =times.split(':')
        H = timess[0]
        M = timess[1]
        S = timess[2]
        H = H.lstrip('0')
        M = M.lstrip('0')
        S = S.lstrip('0')
        H = int(H)
        M = int(M)
        S = int(S)

        sec = sec+S
        if sec > 59:
            sec = sec -60
            min = min+1
        min = min+M
        if min >59:
            min = min - 60
            hr = hr+1
        hr = hr+H

        #print(H,M,S)
        # print(hr,min,sec)
    return ([hr,min,sec])



print(sum_time(["10:33:23","08:29:02","5:08:42"]))