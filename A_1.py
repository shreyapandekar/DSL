students_play_cricekt = []
students_play_badminton = []
students_play_football = []

range_one = int(input("How many students play Cricket: "))
for l in range(range_one):
    name_cricket = str(input("Name of a Student to add in the list: "))
    students_play_cricekt.append(name_cricket)
print(f"Students who play cricket: {students_play_cricekt}\n\n")

range_two = int(input("How many students play Badminton: "))
for m in range(range_two):
    name_badminton = str(input("Name of a Student to add in the list: "))
    students_play_badminton.append(name_badminton)
print(f"Students who play badminton: {students_play_badminton}\n\n")

range_three = int(input("How many students play Football: "))
for n in range(range_three):
    name_football = str(input("Name of a Student to add in the list: "))
    students_play_football.append(name_football)
print(f"Students who play football: {students_play_football}\n\n")

student_play_C_B = []
for i in students_play_cricekt:
    for j in students_play_badminton:
        if i == j:
            student_play_C_B.append(i)
        else:
            pass
print(f"List of Students who play both Cricket and Badminton: {student_play_C_B}")

list_B = []
a = students_play_cricekt
b = students_play_badminton
a, b = [i for i in a if i not in b], [j for j in b if j not in a]
c = a + b
list_B.append(c)
print(f"List of Students who play either Cricket or Badminton but not both: {c}")

list_C = []
combined_list_one = list_B + student_play_C_B
var = combined_list_one
w = var
x = students_play_football
x = [j for j in x if j not in w]
list_C.append(x)
print(f"List of Students who play neither Cricket nor Badminton: {x}")

combined_list_two = students_play_cricekt + students_play_football
p = combined_list_two
q = students_play_badminton
a = [i for i in p if i not in q]
r = a
print(f"List of Students who play Cricket and Football but not Badminton: {r}")
