first = input('Vvedite perve chislo: ',)
second =input('Vvedite vtoroe chislo: ')
third =input('Vvedite tretie chislo: ')
if first==second and second==third:
    print ("3")
elif first==second or second==third or first==third:
    print ('2')
elif first!=second and second!=third:
    print('0')