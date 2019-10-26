n = int(input("Enter the numbers of the students N="))
k = int(input("Enter the numbers of the apples k="))
print("The number of the apples got each students= ", k // n)
print("The numbers of the apples left in the box= ", k - (n * (k // n)))

