#make sure u install this module 
# u can use pip install tabulate in ur shell(and powershells)
import tabulate
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
import numpy as np

def make_table(y, x, y_pred, error, error_times_x):
    table = []
    for i in range(0, len(y)):
        table.append([y[i], x[i], y_pred[i], error[i], error_times_x[i]])
    return table

def minmax_normalize(x):
    x_normal = (x - np.amin(x)) /(np.amax(x) - np.amin(x))
    return x_normal


    


def main():
    y = np.asarray([227, 237, 249, 262])
    y_normal = minmax_normalize(y)
    x = np.asarray([1980, 1985, 1990, 1995])
    x_normal = minmax_normalize(x)
   # l = np.arange(0.0, np.amax(x), 0.02)
    #learning rate or speed
    #note: if u use mse use some r if u use sse use 1/10th of r in mse approx.
    #both are equivalent u only need to change r accordingly
    r = 0.01 #accuracy
    T = 2 # no. of iterations
    n = len(y)
    #normalize the input
    #PASS whatever u want but change r accordingly
    gradient_descent(y, x_normal, n, r, T)

def gradient_descent(y, x, n, r, T):
    #can be any random value
    b1 = round((y[0]-y[1])/(x[0] - x[1]), 2)
    #b1 = -10
    b0 = round(y[0] - b1*x[0], 2)
    #b0 = 300
    y_ = b0 + b1 * x
    print('Learning rate r = %f'%(r))

    current_table = []
    print('b0 init intercept = ', b0)
    print('b1 init slope = ', b1)
    for t in range(0,T):
        print('iteration t = ', t+1)
        if(b1>0):
            print('current y_pred_i = %.2f + %.2fxi'%(b0, b1))
        if(b1<0):
            print('current y_pred_i = %.2f %.2fxi'%(b0, b1))
        y_ = b0 + b1 * x
        error = y - y_
        errorintox = error * x
        sigma_error = np.sum(error)
        sqrerr = error * error
        sse = 1/2 * np.sum(sqrerr)
        print('Square errors:', sqrerr)
        print('Sum of Squared errors(SSE) = ',sse)
        sigma_errintox = np.sum(errorintox)
        current_table = make_table(y, x, y_, error, errorintox)
        print(tabulate.tabulate(current_table, headers=['yi', 'xi', 'y_pred_i', 'yi - y_pred_i', '(yi - y_pred_i)*xi']))
        d1 = round(-1* sigma_errintox,2)
        d0 = round(-1* sigma_error, 2)
        print('d0 = gradient wrt y-intercept = ', d0)
        print('d1 = gradient wrt slope = ', d1)
        b0 -= r * d0
        b1 -= r * d1
        print('b0 = y-intercept = ', b0)
        print('b1 = slope = ', b1)

if __name__ == '__main__':
    main()