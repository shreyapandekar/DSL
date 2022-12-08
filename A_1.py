C=[]
B=[]
F=[]
U=[]
c=int(input("enter number of students who play cricket"))
for i in range(c):
    cri=int(input("enter roll number"))
    C.append(cri)
print("students playing cricket:",C)

b=int(input("enter number of students who play badminton"))
for i in range(b):
    bad=int(input("enter roll numbers who play badminton"))
    B.append(bad)
print("students playing badminton:",B)

f=int(input("enter no of students who play football:"))
for i in range(f):
    foot=int(input("enter roll numbers who play football:"))
    F.append(foot)
print("students playing football:",F)

U.extend(C)
for i in B:
    if i not in U:
        U.append(i)
for j in F:
    if j not in U:
        U.append(j)
print("union of the students:",U)

u=[]
def cribad():
    for i in C:
        for j in B:
            if i==j:
                u.append(j)
    print("students who play both cricket and badminton:",u)
cribad()

m=[]
def cri_bad_notboth():
    for i in C:
        if i not in B:
            m.append(i)
    for j in B:
        if j not in C:
            m.append(j)

    print("students who play either cricket or badminton but not both:",m)
    return(m)
'''cri_bad_notboth()'''

def neither_cri_nor_bad():
    cri_bad=[]
    not_cri_bad=[]
    cri_bad.extend(C)
    for i in B:
        if i not in C:
            cri_bad.append(i)

    for j in U:
        if j not in cri_bad:
            not_cri_bad.append(j)
    print(not_cri_bad)
'''neither_cri_nor_bad()'''

def cri_foot_not_bad():
    cri_foot=[]
    not_bad=[]
    cri_foot.extend(C)
    for i in F:
        if i not in C:
            cri_foot.append(i)

    for j in cri_foot:
        if j not in B:
            not_bad.append(j)
    print(not_bad)
'''cri_foot_not_bad()'''

while(True):

    ch=int(input("enter choice"))
    if(ch==1):
        print("cribad()")
    if(ch==2):
        print("list of students who play either cricket or badminton but not both:",cri_bad_notboth())
    if(ch==3):
        print("number of students who play neither cricket nor badminton:",neither_cri_nor_bad())
    if(ch==4):
        print("number of students who play cricket and football but not badminton:",cri_foot_not_bad())
    if(ch==5):
        exit()
