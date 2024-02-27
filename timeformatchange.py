import time
timestamp=time.strftime('%H,%M,%S')
times=int(time.strftime('%S'))
timeh=int(time.strftime('%H'))
timem=int(time.strftime('%M'))
if (timeh>12):
    x=timeh-12
    print(x,timem,times)
else:
    print(timestamp)
