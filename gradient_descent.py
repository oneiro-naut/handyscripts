#make sure u install this module 
# u can use pip install tabulate in ur shell(and powershells)
import tabulate


def make_table(y, x, y_pred, error, error_times_x):
    table = []
    for i in range(0, len(y)):
        table.append([y[i], x[i], y_pred[i], error[i], error_times_x[i]])
    return table

def main():
    y = [240, 181, 193, 155, 172, 110, 113, 75, 94]
    x = [1.6, 9.4, 15.5, 20.0, 22.0, 35.5, 43.0, 40.5, 33.0]
    n = len(y)
    print(n)
    y_ = [0.0] * n
    error = [0.0] * n
    errorintox = [0.0] * n
    print('y: ', y)
    print('x: ', x)
    #can be any random value
    #b1 = round((y[0]-y[1])/(x[0] - x[1]), 2)
    b1 = -10
    #b0 = round(y[0] - b1*x[0], 2)
    b0 = 300

    #learning rate or speed
    r = 0.0001 #accuracy
    print('Learning rate r = %f'%(r))

    T = 2 # no. of iterations

    current_table = []
    print('b0 init intercept = ', b0)
    print('b1 init slope = ', b1)
    for t in range(0,T):
        print('iteration t = ', t+1)
        if(b1>0):
            print('current y_pred_i = %.2f + %.2fxi'%(b0, b1))
        if(b1<0):
            print('current y_pred_i = %.2f %.2fxi'%(b0, b1))
        sigma_error = 0.0
        sigma_errintox = 0.0
        for i in range(0,n):
            y_[i] = round(b0 + b1 * x[i], 3)
            error[i] = round(y[i] - y_[i], 2)
            errorintox[i] = round(error[i] * x[i], 3)
            sigma_error += error[i]
            sigma_errintox += errorintox[i]
        current_table = make_table(y, x, y_, error, errorintox)
        print(tabulate.tabulate(current_table, headers=['yi', 'xi', 'y_pred_i', 'yi - y_pred_i', '(yi - y_pred_i)*xi']))
        d1 = round(-2/n * sigma_errintox, 2)
        d0 = round(-2/n * sigma_error, 2)
        print('d0 = gradient wrt y-intercept = ', d0)
        print('d1 = gradient wrt slope = ', d1)
        b0 -= r * d0
        b0 = round(b0, 2)
        b1 -= r * d1
        b1 = round(b1, 2)
        print('b0 = y-intercept = ', b0)
        print('b1 = slope = ', b1)

if __name__ == '__main__':
    main()