def digitalClock(sec):
    h = sec//3600
    m = (sec-(3600*h))//60
    s = (sec-(3600*h+m*60))
    print(sec,'seconds is',h,'hours,',m,'mins, ',s,'secs.')


print(digitalClock(5025))