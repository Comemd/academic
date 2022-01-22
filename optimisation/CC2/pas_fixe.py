import pandas as pd

def function(X):
    return X**5 -5*X**3 -20*X +5

def choose(x0,s,ext):
    minus = function(x0-s)
    if ext == 'max':
        if minus < function(x0):
            sens = '+'
        else:
            sens = '-'
    elif ext == 'min':
        if minus < function(x0):
            sens = '-'
        else:
            sens = '+'
    return sens

def after(x,s,sens):
    if sens == '+':
        return x+s
    else:
        return x-s
    
def pas_fixe(x0,s,ext):
    x = x0
    sens = choose(x0, s, ext)
    x_values = []
    func_values = []
    if ext == 'max':
        method = 'maximum'
        while function(after(x,s,sens)) > function(x):
            x_values.append(x)
            func_values.append(function(x))
            x = after(x,s,sens)
        x_values.append(x)
        func_values.append(function(x))
        x = after(x,s,sens)
        x_values.append(x)
        func_values.append(function(x))
        i = func_values.index(max(func_values))
    elif ext == 'min':
        method = 'minimum'
        while function(after(x,s,sens)) < function(x):
            x_values.append(x)
            func_values.append(function(x))
            x = after(x,s,sens)
        x_values.append(x)
        func_values.append(function(x))
        x = after(x,s,sens)
        x_values.append(x)
        func_values.append(function(x))
        i = func_values.index(min(func_values))
    df = pd.DataFrame(list(zip(x_values,func_values)),columns=['xi','f(xi)'])
    print(df)
    print(f'Le {method} trouvé est {function(x_values[i])} à x = {x_values[i]}')
    print('---------------------------------------------------')
    
    
        
    
        