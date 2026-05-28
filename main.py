import numpy as np 

def getMatrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        data = list(map(int,input(f"Enter Elements of Row {i+1} Seperated by Space: ").split()))
        matrix.append(data)
    return np.array(matrix)

def main():
    while True:
        print("Enter Your Choice of Operation: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Inverse")
        print("7. Rank")
        print("8. Trace")
        print("9. Scalar Multiplication")
        print("10. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                print("----------First Matrix----------")
                matrix = getMatrix()
                print("----------Second Matrix----------")
                matrix2 = getMatrix()
                print("The Addition of the two matrices is: ")
                print(matrix + matrix2)
            except Exception as e:
                print(e)
        elif choice == 2:
            try:
                print("----------First Matrix----------")
                matrix = getMatrix()
                print("----------Second Matrix----------")
                matrix2 = getMatrix()
                print("The Subtraction of the two matrices is: ")
                print(matrix - matrix2)
            except Exception as e:
                print(e)
        elif choice == 3:
            try:
                print("----------First Matrix----------")
                matrix = getMatrix()
                print("----------Second Matrix----------")
                matrix2 = getMatrix()
                print("The Multiplication of the two matrices is: ")
                print(matrix @ matrix2)
            except Exception as e:
                print(e)
        elif choice == 4:
                matrix = getMatrix()
                print("Transposed Matrix:")
                print(matrix.T)
        elif choice == 5:
            try:
                matrix = getMatrix()
                det = np.linalg.det(matrix)
                print(f"The Determinant Of Your Matrix Is {det}")
            except Exception as e:
                print(e)
        elif choice == 6:
            try:
                matrix = getMatrix()
                print("Inverse Matrix: ")
                print(np.linalg.inv(matrix))
            except Exception as e:
                print(e)
        elif choice == 7:
            try:
                matrix = getMatrix()
                print("Rank of Matrix is:",end = " ")
                print(np.linalg.matrix_rank(matrix))
            except Exception as e:
                print(e)
        elif choice == 8:
            try:
                matrix = getMatrix()
                print("Trace of Matrix is:",end = " ")
                print(np.trace(matrix))
            except Exception as e:
                print(e)
        elif choice == 9:
            try:
                matrix = getMatrix()
                value = int(input("Enter Scalar Number: "))
                print("Matrix After Scalar Multiplication:")
                print(matrix*value)
            except Exception as e:
                print(e)
        elif choice == 10:
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()