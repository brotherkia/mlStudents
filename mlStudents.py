from importlib.resources import path
import tensorflow as tf
import pandas as pd
from matplotlib import pyplot 


def main():
    path = 'D:\\12-03-22\\f\\Personal\\programing\\py\\usefull stuff\\ml projs\\students\\studentsMath.csv'
    dataset = pd.read_csv(path)
    # numeric_cols1 = ['famrel','freetime','goout','Dalc','Walc','health','absences','G1','G2','G3']
    # categorical_cols =[]
    
    # print(dataset)
    pd.plotting.scatter_matrix(dataset[['G1','sex']])
    pyplot.show()

    
if __name__ == '__main__':
    main()