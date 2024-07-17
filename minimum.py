#FIND THE MINIMUM ELEMENT
list=eval(input("enter the list elements:"))
length=len(list)
min_element=list[0]
min_idx=0
for i in range(1,length):
    if list[i] < min_element:
         min_element=list[i]
         min_idx=i
print("the inputted list is",list)
print("the minimum element in the list is:")
print(min_element,"at index",min_idx)
