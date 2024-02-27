import time 
timestamp=time.strftime('%H,%M,%S')
timeH=int(time.strftime('%H'))
timeM=int(time.strftime('%M'))
timeS=int(time.strftime('%S'))
print(timestamp)
if(timeH>12 and timeH<17):
    print("good afternoon")
elif(timeH==12 and timeM==0):
    print("good noon")
elif(timeH<12):
    print("good morning")
else:
    print("good night")
