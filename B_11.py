#Selection Sort
def SelectionSort(arr,n):
    for i in range(n):
        Min=i
        for j in range(i+1,n):
            if(arr[j]<arr[Min]):
                Min=j
        (array[i], array[Min]) = (array[Min], array[i])
        print(arr)       
#bubble sort                
def BubbleSort(arr,n):
    i=0
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1],arr[j]
        print(arr)
     
#top 5 scores
def Topscores(arr, N): 
    final_list = [] 
    for i in range(0, N): 
        max = 0         
        for j in range(len(arr)):     
            if arr[j] > max: 
                max = arr[j]
        arr.remove(max)
        final_list.append(max) 
    print(final_list) 
    
#main function
array=[]
N=5
i=0
n=int(input("How many students are there?\n"))
for i in range(n):
    print("\nEnter % marks: ")
    item =float(input())
    array.append(item)
    print("You have entered following scores: \n")
    print(array)
     
while(True):
    print("\n1) Selection Sort\n2) Bubble Sort ")
    ch=int(input("Enter your choice: "))
    if (ch==1):
        print("\nThe sorted scores are: ")
        SelectionSort(array,n)
    elif (ch==2):
        print("\nThe sorted scores are: ")
        BubbleSort(array,n)    
    else:
        print("Wrong choice!!!!!!")
    break           

#calling top 5 scores's function
print("\nTop 5 scores are: ")
Topscores(array, N)
