##Searching

student_attend = []
n = int(input("Totle no of students"))
print("Roll no of Students")
for i in range(n):
    student_attend.append(int(input()))
search_element = int(input("Student roll no you want to search"))
student_attend.sort()
start = 0


def LinearSearch(student_attend, search_element):
    for i in student_attend:
        if i == search_element:
            return -1
    return 1


def SentinelSearch(student_attend, search_element):
    for i in range(len(student_attend)):
        if student_attend[i] == search_element:
            print(search_element, "Student Attain lecture", i)
    if (search_element not in student_attend):
        student_attend.pop()
        student_attend.append(search_element)
    print(search_element, "attain the lecture")
    print("new list", student_attend, i)


def BinarySearch(student_attend, search_element):
    start = 0
    end = len(student_attend) - 1
    while start <= end:
        mid = (start + end) // 2
        if student_attend[mid] == search_element:
            return mid
        elif student_attend[mid] < search_element:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def fibonacci(student_attend, search_element):
    fib1, fib2 = 1, 0
    fibn = fib2 + fib1
    student_attend_len = len(student_attend)
    while fibn < student_attend_len:
        fib2 = fib1
        fib1 = fibn
        fibn = fib2 + fib1
    ind = -1
    while fibn > 1:
        n = min(ind + fib2, student_attend_len - 1)
        if student_attend[n] > search_element:
            fibn = fib2
            fib1 = fib1 - fib2
            fib2 = fibn - fib1
        elif student_attend[n] < search_element:
            fibn = fib1
            fib1 = fib2
            fib2 = fibn - fib1
            ind = n
        else:
            return n
    if student_attend[ind + 1] == n and fib1 == 1:
        return ind + 1
    return -1



print("1.Linear\n2.Sentinel\n3.Binary\n4.Fibonacci")
ch = int(input("Enter your choice : "))

if ch == 1:
    result = LinearSearch(student_attend, search_element)
    if result == -1:
        print("Attain the Program")
    else:
        print("Not attain the Program")

elif ch == 2:
    SentinelSearch(student_attend, search_element)

elif ch == 3:
    result = BinarySearch(student_attend, search_element)
    if result == -1:
        print(" not Attain the Program")
    else:
        print("attain the Program")

elif ch == 4:
    result = fibonacci(student_attend, search_element)
    if result == -1:
        print("not Attain the Program")
    else:
        print("attain the Program")
