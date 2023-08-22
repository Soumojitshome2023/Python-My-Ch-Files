r = int(input("Enter numbers of Row : "))
c = int(input("Enter numbers of Coloum : "))
def matrix_input():

    matrix_value = []
    for i in range(1,r+1):
        for j in range(1,c+1):
            a = int(input(f"Enter Row {i} & Coloum {j} element : "))
            matrix_value.append(a)
    n = 0
    for i in range(1,r+1):
        print("\n")
        for j in range(1,c+1):
            print(f"{matrix_value[n]}\t",end='')
            n+=1   

    return matrix_value

print("\nEnter Matrix A : ")
A = matrix_input()

print("\n\nEnter Matrix B : ")
B = matrix_input()


# matrix sum 
print("\n\nSum of Matrix A & B is : ")
n = 0
sum = []
for i in range(1,r+1):
        for j in range(1,c+1):
            sum_matrix = A[n] + B[n]
            sum.append(sum_matrix)
            n+=1
m = 0
for i in range(1,r+1):
    print("\n")
    for j in range(1,c+1):
        print(f"{sum[m]}\t",end='')
        m+=1 