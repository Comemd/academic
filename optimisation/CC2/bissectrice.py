import pandas as pd

def function(X):
    return X**5 -5*X**3 -20*X +5

def following(L,method):
    x0 = (L[0]+L[1])/2
    x1 = (L[0]+x0)/2
    x2 = (x0+L[1])/2
    X = [x1,x0,x2]
    f0 = function(x0)
    f1 = function(x1)
    f2 = function(x2)
    F = [f1,f0,f2]
    if method == 'min':
        if f1 == min(F):
            return [L[0],x0]
        elif f0 == min(F):
            return [x1,x2]
        else:
            return [x0,L[1]]

def bissection(L0,method,e):
    if method == 'min':
        m = 'minimum'
    else:
        m= 'maximum'
    MIN = [L0[0]]
    MAX = [L0[1]]
    L = list(L0)
    while (L[1]-L[0]) > (L0[1]-L0[0])*e:
        L = following(L,method)
        MIN.append(L[0])
        MAX.append(L[1])
    df = pd.DataFrame(list(zip(MIN,MAX)),columns=['min','max'])
    x_final = (L[0]+L[1])/2
    f_final = function(x_final)
    print(df)
    print(f'Le {m} trouvé est {f_final} à x = {x_final}')
    print('---------------------------------------------------')      

        