n=int(input("How Many Days Temperature do you want??"))
ls=[]
for i in range(0,n):
    i=int(input(f"Enter Day {i+1}'s Tempetature "))
    ls.append(i)
avg1=0
for i in ls:
    avg1=avg1+i
avg2=avg1/len(ls)
c=0
for i in ls:
    if i>avg2:
        c=c+1
print(f"Finally there are {c} Days which have temperature more than average temperature")