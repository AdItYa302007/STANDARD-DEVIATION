import csv
import math

with open("Project105.csv",newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

totalMark=0
totalNumber=len(file_data)

new_data=[]
sum=0
for i in range(len(file_data)):
    num=file_data[i][0]
    sum=sum+float(num)

mean=sum/(len(file_data))
print(mean)

sq_list=[]
total=0

for i in range(len(file_data)):
    num=file_data[i][0]
    a=int(num)-mean
    a=a**2
    sq_list.append(a)

for i in sq_list:
    total=total+i

sd=math.sqrt((total/9))
print(sd)
