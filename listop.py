#list operations

#list concatinating using '+' operator
#adding two strings
list1=["red","green"]
list2=[10,20,30]
list1=list1 + ["blue"]
print(list1)

#adding two lists
list=["learn","python"] + ["programming"]
print(list)

#repetition operation
list3=[10,20,30]
print(list2*2)

x="python"*3
print(x)

#indexing operation
list4=["red","blue","green"]
list5=[10,20,30,40,50]
print(list4[2])
print(list5[-2])

#slicing operation
list6=[100,500.75,"radhika","shauraya",900,897.60]
print(list1[:])
print(list6[2:5])
print(list5[-2:-5:-1])

#append
l1=[10,20,30,40]
l1.append(55)
print(l1)

#extend
l2=[5,3,8,6]
l3=[13,14]
l2.extend(l3)
print(l2)

#insert
names=['vijay','sonia','shhaurya','radhika']
names.insert(2,'deepak')
print(names)

#reverse
age=[15,16,17,18,19,20]
age.reverse()
print(age)

#update
l4=[1,2,3]
l4[1]=4
print(l4)

#len
l5=[8,"sakshi","shivam",23,16]
print(len(l5))

#sort
l6=[10,4,20,98,2,100]
l6.sort()
print(l6)

#clear
l7=[23,34,45,67,78]
l7.clear()
print(l7)

#count
l8=['a',('x','y'),[1,2],'b',10,[1,2]]
l8.count([1,2])
l8.count(('x','y'))
l8.count(100)

#deletion operation
#pop()
l9=[1,2,34,34,56,5,67,11,90]
a=l9.pop(5)
print(l9)

#del()
l10=[10,20,30,40,50]
del l10[2:4]
print(l10)

#remove()
l11=[23,65,98,45,66]
l11.remove(98)
print(l11)
