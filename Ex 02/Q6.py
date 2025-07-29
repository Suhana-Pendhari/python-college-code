# Q6) Matrix Operations:
# Write a script that performs matrix addition or multiplication based on 
# user input. Use nested loops (for loops) to iterate through matrix elements.

op = input("Enter 'add' for addition or 'mul' for multiplication: ")

if op == 'add':
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    print("Enter matrix A:")
    A = []
    for i in range(rows):
        row = list(map(int, input().split()))
        A.append(row)
    print("Enter matrix B:")
    B = []
    for i in range(rows):
        row = list(map(int, input().split()))
        B.append(row)

    print("Result of addition:")
    for i in range(rows):
        for j in range(cols):
            print(A[i][j] + B[i][j], end=' ')
        print()
elif op == 'mul':
    rows_A = int(input("Matrix A rows: "))
    cols_A = int(input("Matrix A columns: "))
    rows_B = int(input("Matrix B rows: "))
    cols_B = int(input("Matrix B columns: "))
    if cols_A != rows_B:
        print("Cannot multiply: columns of A must equal rows of B.")
    else:
        print("Enter matrix A:")
        A = []
        for i in range(rows_A):
            row = list(map(int, input().split()))
            A.append(row)
        print("Enter matrix B:")
        B = []
        for i in range(rows_B):
            row = list(map(int, input().split()))
            B.append(row)
        print("Result of multiplication:")
        for i in range(rows_A):
            for j in range(cols_B):
                sum = 0
                for k in range(cols_A):
                    sum += A[i][k] * B[k][j]
                print(sum, end=' ')
            print()
else:
    print("Invalid operation.")

