grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted (students)
print (students)
a = sum (grades [0])/len (grades[0])
s = sum (grades [1])/len (grades[1])
b  = sum (grades [2])/len (grades[2])
c  = sum (grades [3])/len (grades[3])
d = sum (grades [4])/len (grades[4])
grades = [a, s,b,c,d]
res = {students[i]: grades[i] for i in range(len(grades))}
print (res)