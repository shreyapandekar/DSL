##FINAL
x = int(input("Enter no.of rows: "))
y = int(input("Enter no. of columns: "))
x1 = []
y1 = []

def printMat(x, y, result):
    for i in range(x):
        for j in range(y):
            print(result[i][j], end=' ')
        print()

def inputMatrix1(x, y):
    x1 = []
    print("\nEnter the elements for 1st matrix : ")
    for i in range(0, x):
        m1 = []
        for j in range(0, y):
            print([i], [j])
            m1.append(int(input()))
        x1.append(m1)
    return x1

def inputMatrix2(x, y):
    y1 = []
    print("\nEntet the elements for 2nd matrix : ")
    for i in range(0, x):
        m2 = []
        for j in range(0, y):
            print([i], [j])
            m2.append(int(input()))
        y1.append(m2)
    return y1

x1 = inputMatrix1(x, y)
y1 = inputMatrix2(x, y)

print("\n1st Matrix")
for _ in range(x):
    print (x1[_],end=" ")
    print ()

print("\n2nd Matrix")
for _ in range(y):
    print (y1[_],end=" ")
    print ()
    
def Addition(x, y, x1, y1):
    result = []
    for i in range(x):
        ans = []
        for j in range(x):
            ans.append(x1[i][j] + y1[i][j])
        result.append(ans)
    print("\nAddition is ")
    printMat(x, y, result)

def Subtraction(x, y, x1, y1):
    result = []
    for i in range(x):
        ans = []
        for j in range(x):
            ans.append(x1[i][j] - y1[i][j])
            result.append(ans)
    print("\nSubtraction is ")
    printMat(x, y, result)

def Product(x, y, x1, y1):
    result = [[0 for i in range(y)] for i in range(x)]

    for i in range(x):
        for j in range(y):
            for k in range(y):
                result[i][j] += x1[i][k] * y1[k][j]
    print("\nMultiplication ")
    printMat(x, y, result)

def Transpose1(x, y, x1):
    result = []
    for i in range(x):
        ans = []
        for j in range(y):
            ans.append(x1[j][i])
        result.append(ans)

    print("\nTranspose of x1 ")
    printMat(x, y, result)

def Transpose2(x, y, y1):
    result = []
    for i in range(x):
        ans = []
        for j in range(y):
            ans.append(y1[j][i])
        result.append(ans)
    print("\nTranspose of y1 ")
    printMat(x, y, result)


while True:
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Transpose of x1\n5.Transpose of y1")
    ch = int(input("\n\nchoose operation: "))
    if ch == 1:
        Addition(x, y, x1, y1)
    elif ch == 2:
        Subtraction(x, y, x1, y1)
    elif ch == 3:
        Product(x, y, x1, y1)
    elif ch == 4:
        Transpose1(x, y, x1)
    elif ch==5:
        Transpose2(x,y,y1)
        quit()
    else:
        print("Invalid")
