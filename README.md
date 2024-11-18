# Python Math and Matrix Operations

This repository contains Python functions to perform various mathematical and matrix operations. The code is implemented both as a Python script (`.py` file) and in a Jupyter Notebook for interactive use.

---

## **Features**

### **Mathematical Operations**
1. **Fibonacci Sequence**  
   Generate the first `n` numbers in the Fibonacci sequence.

2. **HCF (Highest Common Factor)**  
   Compute the HCF of two numbers.

3. **GCD (Greatest Common Divisor)**  
   Identical to HCF, as per the mathematical definition.

4. **LCM (Least Common Multiple)**  
   Compute the LCM of two numbers using the relationship:  
   \[ \text{LCM}(a, b) = \frac{|a \times b|}{\text{HCF}(a, b)} \]

### **Matrix Operations**
5. **Add Two Matrices**  
   Add two matrices of the same dimensions element-wise.

6. **Transpose a Matrix**  
   Compute the transpose of a matrix.

7. **Multiply Two Matrices**  
   Multiply two matrices using the standard row-column dot product method.

---

## **Setup Instructions**

### **Requirements**
- Python 3.6 or higher
- Jupyter Notebook (optional, for interactive use)

### **Run as a Python Script**
1. Clone the repository:
   ```bash
   git clone https://github.com/py_problems.git
   
2. Run the Python script:
   ```bash
   python math_operations.py

### **Run in Jupyter Notebook**
1. Install Jupyter Notebook if not already installed:
   ```bash
   pip install notebook

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   
3. Open the provided notebook file and interact with the functions.

---
## **Usage**
1. Fibonacci Sequence:
   ```python
   from math_operations import fibonacci
   print(fibonacci(10))
   # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

2. Matrix Addition:
   ```python
   from math_operations import add_matrices
   matrix1 = [[1, 2], [3, 4]]
   matrix2 = [[5, 6], [7, 8]]
   print(add_matrices(matrix1, matrix2))
   # Output: [[6, 8], [10, 12]]
   
---
## **File Structure**

```plaintext
.
├── math_operations.py      # Python script with all functions
├── math_operations.ipynb   # Jupyter Notebook with all functions
├── client.py               # Script to call and demonstrate functions
├── README.md               # Documentation
