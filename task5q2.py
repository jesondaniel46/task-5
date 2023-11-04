n = 20  # Set the number of rows for the pyramid

for i in range(1, n + 1):
    # Print spaces before the numbers
    for j in range(n, i, -1):
        print(" ", end=" ")
    
    # Print numbers in ascending order
    for k in range(1, i):
        print(k, end=" ")
    
    # Print numbers in descending order
    for l in range(i, 0, -1):
        print(l, end=" ")
    
    # Move to the next line for the next row
    print()
