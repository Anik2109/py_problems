from math_operations import (
    fibonacci,
    hcf,
    lcm,
    add_matrices,
    transpose_matrix,
    multiply_matrices,
)

def main():
    print("Fibonacci Sequence:")
    n = 10
    print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")

    print("\nHCF (Highest Common Factor):")
    a, b = 60, 48
    print(f"The HCF of {a} and {b} is: {hcf(a, b)}")

    print("\nLCM (Least Common Multiple):")
    x, y = 15, 20
    print(f"The LCM of {x} and {y} is: {lcm(x, y)}")

    print("\nMatrix Addition:")
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    print(f"Matrix 1: {matrix1}")
    print(f"Matrix 2: {matrix2}")
    print(f"Result: {add_matrices(matrix1, matrix2)}")

    print("\nMatrix Transpose:")
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(f"Original Matrix: {matrix}")
    print(f"Transposed Matrix: {transpose_matrix(matrix)}")

    print("\nMatrix Multiplication:")
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    print(f"Matrix A: {matrix_a}")
    print(f"Matrix B: {matrix_b}")
    print(f"Result: {multiply_matrices(matrix_a, matrix_b)}")

if __name__ == "__main__":
    main()
