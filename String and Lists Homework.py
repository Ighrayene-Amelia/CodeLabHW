
list=[]
for i in range(1,299):
    if i%2==0:
        list.append(i) 
print("The even numbers are: ")
print(list) 

a=0 
for i in list:
    a+=1
print("\n the length of this list is: ",a)

print("\n the squared values of the list are: ")
for i in list:
    if (i**0.5).is_integer():
        print( i,end=" ")

print("\n",57 in list)