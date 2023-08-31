def digitalClock(sec):
    h = sec//3600
    m = (sec-(3600*h))//60
    s = (sec-(3600*h+m*60))
    if h//24 >=1:
      h = h%24
    formatted_time = "{:02d}:{:02d}:{:02d}".format(h, m, s)
    return formatted_time

print(digitalClock(5025))    



print(digitalClock(61201))


print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))
print(digitalClock(176470))