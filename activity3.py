c1 = 20
c2 = 20
c3 = 20
avg = (c1+c2+c3)/3
if c1 < avg:
    print("The first cyclist is slower than the average")
elif c2 < avg:
    print("The second cyclist is slower than the average") 
elif c3 < avg:
    print("The third cyclist is slower than the average")
else:
    print("All cyclists are either equal to or faster than the average")