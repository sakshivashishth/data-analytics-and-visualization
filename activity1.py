import pandas as pd
dict1={'stdid':['std101','std102','std103','std104','std105','std106','std107','std108','std109','std110'],
       'stdname':['ashish kumar','abhishek kumar','aman','rahul','ruby','suman','saurabh','sumit','kamlesh','rohan'],
       'standard':['10th','10th','10th','10th','10th','10th','10th','10th','10th','10th'],
       'age':[15,14,15,14,13,13,15,14,15,15],
       'hindi':[67,85,23,45,89,90,45,23,45,34],
       'english':[89,45,56,67,67,46,23,45,56,12],
       'maths':[87,48,78,45,89,67,34,67,78,24],
       'science':[89,90,78,45,93,67,45,78,99,45],
       'computer':[90,45,67,56,65,67,34,90,67,56],
       'total':[422,313,302,258,403,337,181,303,345,171]}


'''print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} ".format('stdid', 'stdname', 'standard','age','hindi','english','maths','science','computer','total'))
for key, value in dict1.items():
    stdid,stdname,standard,age,hindi,english,maths,science,computer,total = value
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(stdid,stdname,standard,age,hindi,english,maths,science,computer,total))
'''
df=pd.DataFrame(dict1)
print(df)
print("students whose marks are greater than 50 are as follows:")
ans1=df[df['english']>50]
print(ans1)
print("top 4 scorer of maths")

ans2 = df.nlargest(4,'maths')[['stdname','age']]
print(ans2)

