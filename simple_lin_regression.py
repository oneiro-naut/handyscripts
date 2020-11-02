import tabulate

import numpy as np

def make_table(y, x, yx, xsqr,y_pred,error):
    table = []
    for i in range(0, len(y)):
        table.append([y[i], x[i], yx[i], xsqr[i], y_pred[i],error[i]])
    return table



def main():  
    y = np.asarray([240, 181, 193, 155, 172, 110, 113, 75, 94])
    x = np.asarray([1.6, 9.4, 15.5, 20.0, 22.0, 35.5, 43.0, 40.5, 33.0])
    n = len(y)
    sigma_x = np.sum(x)
    x_avg = sigma_x / n
    sigma_y = np.sum(y)
    y_avg = sigma_y / n
    yx = y * x
    xsqr = x * x
    sigma_yx = np.sum(yx)
    sigma_xsqr = np.sum(xsqr)
    b1 = (sigma_yx - sigma_y * sigma_x / n)/ (sigma_xsqr - (sigma_x)**2 /n)
    b0 =  y_avg - b1 * x_avg
    y_pred = b0 + b1 * x
    error = y - y_pred
    table = make_table(y,x,yx,xsqr,y_pred,error)
    print(tabulate.tabulate(table, headers=['yi','xi','yixi','xisqr','y_pred','error=y - y_pred']))
    print('sigma x = %f sigma y = %f sigma yx = %f sigma xsqr = %f'%(sigma_x,sigma_y,sigma_yx,sigma_xsqr))
    print('b0 = %f , b1 = %f'%(b0,b1))




if __name__ == '__main__':
    main()
