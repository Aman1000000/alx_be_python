size = int(input ("Enter the size of the pattern: "))
row = 0
counter = 0
asterisk = "*"

while counter < size:
    row = 0  
    while row < size:
        print("*", end = " ")  
        row += 1
    print()  
    counter += 1