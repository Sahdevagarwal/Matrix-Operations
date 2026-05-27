import numpy as np 

def getMatrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        data = []
        for j in range(cols):
            element = int(input(f"Enter Element [{i + 1}][{j + 1}]: "))
            data.append(element)
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
        elif choice == 10:
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()