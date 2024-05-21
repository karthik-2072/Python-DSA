import numpy as np
a=np.array([11,2,34,4],dtype=int)
print(a)

def traverseArray(tl):
    print("Array Traversing")
    for i in tl:
        print(i)
def accessElemnt(ls,ind):
    if ind>=len(ls):
        print("Index out of range")
    else:
        print(f"Element at {ind} index is : {ls[ind]}")
def linear_search(ls,target):
    flag=0
    for i in range(0,len(ls)):
        if ls[i]==target:
            print(f"Element is at index {i}")
            flag=1
    if flag==0:
        print("Not Found")


from array import *
ls=array('i',[1,2,3,4])
print(ls)
ls.insert(3,120)
print(ls)
#traverseArray(ls)
#accessElemnt(ls,5)
#linear_search(ls,1)
ls.insert(5,45)
print("Before Removal")
print(ls)
ls.remove(45)#45 is removed from array
print("after Removal")
print(ls)
ls.append(2072)
print("After appending")
print(ls)

ls1=array('i',[540,541,542])
ls.extend(ls1)
print("after extending ",ls)

tempList = [20,21,22]
ls.fromlist(tempList)
print(ls)

ls.reverse()
print(ls)


#2D Arrays

def accessEle(ls,row,column):
    print(f"element is {ls[row][column]}")
def traverseArray(ls):
    for i in range(0,len(ls)):
        for j in range(0,len(ls[0])):
            print(f"element at row {i} column {j} is {ls[i][j]}")
def linear_search(ls,target):
    flag=0
    for i in range(0,len(ls)):
        for j in range(0,len(ls[0])):
            if ls[i][j]==target:
                print(f"element found at {i} {j} index")
                flag=1
    if flag==0:
        print("element not found")
import numpy as np
twoD=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoD)

print(twoD[0][1])

twoD=np.insert(twoD,0,[[10,11,12]],axis=1)
print(twoD)

accessEle(twoD,1,2)
traverseArray(twoD)
linear_search(twoD,11)
print(twoD)
twoD=np.delete(twoD,0,axis=1)
print(twoD)