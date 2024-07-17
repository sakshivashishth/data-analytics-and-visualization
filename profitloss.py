cp=float(input("enter cost price"))
sp=float(input("enter selling price"))
if(cp>=0 and sp>=0):
    if(cp>sp):
        loss=cp-sp
        print(loss)
    elif(cp<sp):
       profit=sp-cp
       print(profit)
    else:
        print("no profit no loss")
else:
    print("price must  be positive")
    
