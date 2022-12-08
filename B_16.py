def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def partition(arr,start,end):
    pivot = arr[end]
    i=start-1
    for j in range(start,end):
        if(arr[j]<pivot):
            i=i+1
            swap(arr,i,j)
    swap(arr,(i+1),end)
    return (i+1)

def quick_sort(arr,start,end):
    if (start<end):
        pivot = partition(arr,start,end)
        
        print("Quick Sort: ",arr)
        quick_sort(arr,start,(pivot-1))
        quick_sort(arr,(pivot+1),end)

cont='y'    
while(cont=='y'):
    n=int(input("Enter the no. of students: "))
    if(n<5):
        while(n<5):
            print("Sorry, Number of students can not be less than 5")
            n=int(input("Enter the no. of students again: "))
    a=[]
    for i in range(n):
        print("Enter percentage student",i,": ",end="")
        elem=float(input())
        if((elem<=100) and (elem>=0)):
            a.append(elem)
        else:
            while((elem>100) or (elem<0)):
                print("Percentage can not be greater than 100 or negative")
                print("Enter percentage studnet",i," again: ",end="")
                elem=float(input())
            a.append(elem)
    print("List of percentage of students is: ",a,"\n")  
    quick_sort(a,0,(n-1))
    print("The sorted list of percentages (by Quick Sort) is: ",a)
    print("The Top 5 scores are:")
    for i in range(n-1,n-6,-1):
        print(n-i,"th: ",a[i])
    cont=input("Do you want to continue? (y/n): ")
if(cont=='n'):
    print("Thank you!!!")
