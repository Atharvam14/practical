dict1={}

while True:
    data = input("Enter the name and mobile number seperated by comma: ")
    if 'Exit' == data:
        break
    name,num=data.split(",")
    num = int(num)
    dict1[num]=name
print(dict1)
list1=dict1.keys()
list1=list(list1)
list1.sort()
print(list1)


key = int(input("The number to search for: "))

print("Binary Search Using Non-Recursive Method\n")

"""
Non Recursive Function
"""
def binary_search1(list1,key):
   start=0
   end=len(list1)
   
   while start<end :
   
       mid=(start+end)//2
       
       if list1[mid]<key :
           end=mid
           
       elif list1[mid]<key :
           start=mid+1
           
       else:
           return mid
           
   return-1
    
    
    
index=binary_search1(list1,key)
if index<0:
    print("{} was not found.".format(key))
else:
    print("{} was found at index {}.".format(key,index))
    print("Details of number found: ")
    print(dict1[key])
    
    
    
"""
Recursive Function
"""
def binary_search(arr,low,high,x):

    #check base case
    if high>=low:
        
        mid=(high+low)//2
        
        #If element is present at middle itself
        if arr[mid]==x:
            return mid
            
        #If element is smaller than mid, then it can only
        #be present in left subarray
        if arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
            
        #Else the element can only be present in right subarray
        else:
            return binary_search(arr,low,mid+1,x)
            
    else:
        #element is not present in the array
        return-1
        
#Test Array
while True:
    data = input("Enter the name and mobile number seperated by comma: ")
    if 'Exit' == data:
        break
    name,num=data.split(",")
    num = int(num)
    dict1[num]=name
print(dict1)
list1=dict1.keys()
list1=list(list1)
list1.sort()
print(list1)

key=int(input("The number to search for: "))

print("Binary Search Using Recursive Method\n")

#Function call
result=binary_search(list1,0,len(list1)-1,key)

if result!=1:
    print("Element is present at index: ", str(result))
else:
    print("Element is not present in array")
    
    
    
data1=input("Enter name and mobile number not present in array: ")
name,num=data1.split(",")
num = int(num)
dict1[num]=name

print(dict1)
list1=dict1.keys()
list1=list(list1)
list1.sort()
print(list1)

dict1={}


while True:
    data = input("Enter the name and mobile number seperated by comma: ")
    if 'Exit' == data:
        break
    name,num=data.split(",")
    num = int(num)
    dict1[num]=name
print(dict1)
list1=dict1.keys()
list1=list(list1)
list1.sort()
print(list1)
n=len(list1)
key=int(input("The number to search for: "))


def insert(list1,key):
    num=int(key)
    name=input("Enter name: ")
    dict1[num]=name
    
    
def fibSearch(list1,key,n):

    #Initialize fibonacci numbers
    f2=0    #(m-2)'th Fibonacci No.
    f1=1    #(m-1)'th Fibonacci No.
    fibM=f2+f1    #m'th Fibonacci No.

    #fibM is going to store the smallest
    #Fibonacci number greater than or equal to n
    while(fibM<n):
        f2=f1
        f1=fibM
        fibM=f2+f1
        
    #Marks the eliminated range from front
    offset=-1
    
    #While there are elements to be inspected
    #Note that we compare list1[f2] with key.
    #When fibM becomes 1, f2 becomes 0
    while (fibM>1): 
    
        #Check if f2 is a valid location
        i=min(offset+f2,n-1)
        
        #If key is greater than the value at index f2,
        #cut the subarray from offset to i 
        if (list1[i]<key):
            fibM=f1
            f1=f2
            f2=fibM-f1
            offset=i
        
        #If key is less than the value at index f2,
        #cut the subarray after i+1
        elif (list1[i]>key):
            fibM=f2
            f1=f1-f2
            f2=fibM-f1
            
        #Element found. Return index    
        else:
            return i
            
    #Comparing the last element wwith key*/
    if(f1 and list1[offset+1]==key):
        return offset+1;
        
    #Element not found. Return-1
    return-1
    
    
#Driver code
"""
arr=[10,22,35,40,45,50,80,82,85,90,100]
n=len(arr)
x=85
"""

result=fibSearch(list1,key,n)

if result!=1:
    print("Element is present at index:", str(result))
    
else:
    print(key,"is not in the phonebook")
    print("Record",key,"is now inserted in phonebook...")
    insert(list1,key)
    
    
    print("Record",key,"added successfully in phonebook...")      
    print(dict1)
list1=dict1.keys()
list1=list(list1)
list1.sort()
print(list1)      
