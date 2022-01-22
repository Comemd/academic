import pandas as pd

def function(X):
    return X**3 -7*X**2 +8*X -3

def derivate1(X):
    return 3*X**2 -14*X +8

def derivate2(X):
    return 6*X - 14

def after(X):
    return X - derivate1(X)/derivate2(X)

def newton_raphson(x,e):
    y = x
    L_x = [y]
    L_f1 = [abs(derivate1(y))]
    L_f = [function(y)]
    while abs(derivate1(y)) >= e:
        y = after(y)
        L_x.append(y)
        L_f1.append(derivate1(y))
        L_f.append(function(y))
    df = pd.DataFrame(list(zip(L_x,L_f1,L_f)),columns=['xi',"|f'(xi)|",'f(xi)'])
    if L_f[len(L_f)-1] < L_f[len(L_f)-2]:
        method = 'minimum'
    else:
        method = 'maximum'
    print(df)
    print(f'Le {method} trouvé est {L_f[len(L_f)-1]} à x = {L_x[len(L_x)-1]}')
    print('---------------------------------------------------')


