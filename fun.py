import numpy
import random
from matplotlib import pyplot

def foo(num_iter ,c ):
    matrix = numpy.zeros((200,200))
    rows, columns = matrix.shape
    for row in range(0,rows,random.randint(1,7)):
        for column in range(0,columns,random.randint(1,7)):
            matrix[row,column] = random.random()
    for i in range(num_iter):
        for row in range(rows-1):
            for column in range(columns-1):
                if (matrix[row, column]>0.9):
                    matrix[row-1, column] = c*matrix[row, column]
                    matrix[row+1, column] = c*matrix[row, column]
                    matrix[row, column-1] = c*matrix[row, column]
                    matrix[row, column+1] = c*matrix[row, column]
        ax = pyplot             
        fig = ax.imshow(matrix)
        m2 = matrix[40:60,40:60]
    return fig

foo(100, 0.9)

