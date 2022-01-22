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

def nb(x0,s0,sens,i):
    if sens == '+':
        return x0+(s0*2**i)
    else:
        return x0-(s0*2**i)
    
def pas_accéléré(x0,s0,ext):
    i = 0
    x = x0
    x_values = [x0]
    func_values = [function(x0)]
    sens = choose(x0, s0, ext)
    if ext == 'max':
        method = 'maximum'
        while function(nb(x0,s0,sens,i+1)) > function(nb(x0,s0,sens,i)):
            x = nb(x0,s0,sens,i+1)
            x_values.append(x)
            func_values.append(function(x))
            i+=1
    elif ext == 'min':
        method = 'minimum'
        while function(nb(x0,s0,sens,i+1)) < function(nb(x0,s0,sens,i)): 
            x = nb(x0,s0,sens,i+1)
            x_values.append(x)
            func_values.append(function(x))
            i+=1
    df = pd.DataFrame(list(zip(x_values,func_values)),columns=['xi','f(xi)'])
    print(df)
    print(f'Le {method} trouvé est {function(x_values[len(x_values)-1])} à x = {x_values[len(x_values)-1]}')
    print('---------------------------------------------------')    
    
        