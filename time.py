sec=int(input("enter time in seconds"))
if(sec>=0):
    hours=0
    min=0
   #conversion of sec in hours 
    if(sec>=3600):
        hours= sec//3600

        sec=sec%3600
   #conversion of sec into minute
    if(sec>=60):
       min=sec//60
       sec=sec%60
    print(hours,"hours",min,"minutes",sec,"seconds")
else:
    print("time cannot be negative")

