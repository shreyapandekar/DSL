# Main function
Marks=[]
numberofstudents=int(input("Enter total number of students : "))
for i in range(numberofstudents):
    marks=int(input("Enter marks of student "+str(i+1)+" : "))
    Marks.append(marks)

def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
            sum+=listofmarks[i]
            count+=1
    avg=sum/count
    print("Total Marks : ", sum)
    print("Average Marks :{:.2f}".format(avg))

# Function for Highest score in the test for the class
def Maximum(listofmarks):
    for i in range(len(listofmarks)):
            Max=listofmarks[0]
    for i in range(len(listofmarks)):
        if listofmarks[i]>Max:
            Max=listofmarks[i]
    return(Max)

# Lowest score in the test
def Minimum(listofmarks):
    for i in range(len(listofmarks)):
            Min=listofmarks[0]
    for i in range(len(listofmarks)):
        if listofmarks[i]<Min:
            Min=listofmarks[i]
    return(Min)

# counting the number of students absent for the test
def absentcount(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]==-1:
            count+=1
    return(count)

#Marks with highest frequency
def maxFrequency(listofmarks):
    i=0
    Max=0
    print("Marks  |  Frequency")
    for j in listofmarks:
            if (listofmarks.index(j)==i):
            	print(j,"    |  ",listofmarks.count(j)) 
            	if listofmarks.count(j)>Max:
                	 Max=listofmarks.count(j)
                	 mark=j
            i=i+1
    return(mark,Max)

while True:
    print("1. Total and Average Marks of the Class")
    print("2. Highest and Lowest Marks in the Class")
    print("3. Number of Students absent for the test")
    print("4. Marks with Highest Frequency")
    ch=int(input("Enter your Choice (from 1 to 4) :"))

    if ch==1:
        average(Marks)

    elif ch==2:
        print("Highest Score in Class : ", Maximum(Marks))
        print("Lowest Score in Class : ", Minimum(Marks))

    elif ch==3:
        print("Number of Students absent in the test : ", absentcount(Marks))
        
    elif ch==4:
        mark,fr = maxFrequency(Marks)
        print("Highest frequency is of marks {0} that is {1} ".format(mark,fr))
    else:
        print("!!Wrong Choice!! ")

           
