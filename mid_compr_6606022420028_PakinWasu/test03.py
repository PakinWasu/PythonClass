def time_sum(*time):
    hr =0
    min =0
    sec =0
    for ti in time:
        pass
    for times in ti:
        times = times.split(':')
        H = times[0]
        M = times[1]
        S = times[2]
        H = H.lstrip('0')
        M = M.lstrip('0')
        S = S.lstrip('0')
        H = int(H)
        M = int(M)
        S = int(S)
        sec = sec+S
        if sec > 59:
            sec = sec - 60
            min = min+1
        min = min+M
        if min > 59:
            min = min -60
            hr = hr+1
        hr = hr+H            
        #print(H,M,S)  
        #print(hr,min,sec)
    return([hr,min,sec])
print(time_sum(["1:23:45"]))
print(time_sum(["1:03:45",'1:23:05']))
print(time_sum(["5:39:42",'10:02:08',"8:26:33"]))