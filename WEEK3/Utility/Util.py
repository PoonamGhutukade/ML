import numpy as np


class UtilClass:
    """1. Write a python program to add below matrices """

    @staticmethod
    def matrix_addtn(matrix1, matrix2, result):
        # iterate throw row
        for temp in range(len(matrix1)):
            a = matrix1[temp]

            # iterate throw column
            for temp2 in range(len(matrix1[0])):
                result[temp][temp2] = a[temp] + matrix2[temp][temp2]
                result[temp][temp2] = matrix1[temp][temp2] + matrix2[temp][temp2]

        return result

    """4. Write a program to multiply matrices in problem 1"""

    # matrix multiplication using zip
    def matrix_multiplication(self, matrix1, matrix2):
        result = [[sum(row * col for row, col in zip(matrix1_row, matrix2_col))
                   for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
        return result

    # matrix multiplication thought for loops
    def multi(self, matrix1, matrix2, result14):
        # iterate by row of matrix1
        for temp in range(len(matrix1)):

            # iterating by coloum of matrix2
            for jtemp in range(len(matrix2[0])):

                # iterating by rows of matrix2
                for kval in range(len(matrix2)):
                    # calculate multiplication & store result
                    result14[temp][jtemp] += matrix1[temp][kval] * matrix2[kval][jtemp]
        return result14

    """2.Write a program to perform scalar multiplication of matrix and a number"""

    # scalar matrix multiplication method
    @staticmethod
    def matrix_scalar_multi(matrix1, result):
        # number multiply with each value into array
        num = 9
        # iterate throw row
        for temp in range(len(matrix1)):
            # iterate throw column
            for temp2 in range(len(matrix1[0])):
                # calculate multiplication & store result
                result[temp][temp2] = num * matrix1[temp][temp2]
        return result

    """3. Write a program to perform multiplication of given matrix and vector"""

    # multiplication of given matrix1 and vector
    def vector12(self, vector1, matrix1):
        # calculate length of vector and matrix
        row = len(vector1)
        mat = len(matrix1)
        # use zero matrix to store result into it
        multi = [0] * mat
        sum1 = 0
        # iterate throw row
        for temp in range(mat):
            row1 = matrix1[temp]

            # iterate throw column
            for temp2 in range(row):
                # calculate multiplication & store result
                sum1 += row1[temp2] * vector1[temp2]

            multi[temp] = sum1
            sum1 = 0
        return multi

    """5. Write a program to find inverse matrix of matrix X in problem 1"""

    def inverse_matrix(self, matrix1):
        return np.linalg.inv(matrix1)

    """	6. Write a program to find transpose matrix of matrix Y in problem 1 """
    # transpose matrix using list comprehension
    def transpose_matrix(self, matrix1):
        # use list comprehension
        rez = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
        print("\n")
        for row in rez:
            print(row)

    # transpose matrix using zip
    def trans_matrix(self, matrix1):
        # using zip, show result into tuple
        t_matrix = zip(*matrix1)
        for row in t_matrix:
            print(row)

    # transpose matrix using numpy
    def transpose(self, matrix1):
        # use numpy inbuilt methods
        return np.transpose(matrix1)
