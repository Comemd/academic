import pandas as pd


class variables():
    """Creates a list of the variables"""
    
    def __init__(self,nb):
        self.liste = []
        self.number = nb
        
        print()
        print("-----------------------------------------------")
        print("Creating variables")
        for i in range(self.number):
            v = input(f'What is the name of the variable {i+1} ? : ')
            self.liste.append(v)
    
class constrincts():
    """Creates a list of the constrincts"""
    
    def __init__(self,nb,variables):
        self.liste = []
        self.number = nb
        self.liste_vari = variables.liste
        self.nb_vari = len(self.liste_vari)
        self.comp = []
        
        for k in range(self.number):
            print()
            print("-----------------------------------------------")
            print("Creating constrinct")
            C = []
            for i in range(self.nb_vari):
                n = input(f"What is the {self.liste_vari[i]} coefficient in this constrinct ? : ")
                C.append(int(n))
            c1 = input("Which comparison ? : ")
            c2 = input("Compared to ? : ")
            C.append(int(c2))
            self.comp.append(c1)
            self.liste.append(C)
    
class function():
    """Generates a list representing the function"""
    def __init__(self,variables):
        self.liste = []
        self.liste_vari = variables.liste
        self.nb_vari = len(self.liste_vari)
        
        print()
        print("-----------------------------------------------")
        print("Creating function")
        for i in range(self.nb_vari):
            n = input(f"What is the {self.liste_vari[i]} coefficient in the function ? : ")
            self.liste.append(int(n))

class tables():
    
    def __init__(self,vari,func,con,method):
        self.vari = vari.copy()
        self.nb_vari = len(self.vari)
        if method == 'maxi':
            self.func = func
        else:
            self.func = [-x for x in func]
        self.con = con[:-1]
        self.nb_con = len(self.con)
        self.table = []
        self.lines_taken = []
        self.pivot = []
        
        self.comp = con[len(con)-1]
        self.nb_less = self.comp.count('<=')
        self.nb_equal = self.comp.count('=')
        self.nb_greater = self.comp.count('>=')

        self.basi = [f'e{i}' for i in range(0,self.nb_less + self.nb_greater)]
        self.nb_basi = len(self.basi)
        self.arti = [f'a{i}' for i in range(0,self.nb_greater+self.nb_equal)]
        self.nb_arti =len(self.arti)
        self.all_vari = self.vari + self.basi + self.arti
        
        self.bas = []
        self.non_bas = []
        
        L1 = [-1*k for k in self.func]
        L1.append(0)
        self.table.append(L1)
        
        for k in self.con:
            self.table.append(k)
        
        self.table[0].insert(len(self.table[0])-1,1)
        for k in range(self.nb_basi+self.nb_arti):
            self.table[0].insert(self.nb_vari,0)
        
        for i in range(1,len(self.table)):
            self.table[i].insert(len(self.table[i])-1,0)
        
        for i in range(1,len(self.table)):
            for j in range(self.nb_basi+self.nb_arti):
                self.table[i].insert(self.nb_vari,0)
        
        ek = self.nb_vari
        ak = self.nb_vari+self.nb_basi
        for i in range(1,len(self.table)):
            if self.comp[i-1] == '<=':
                self.table[i][ek] = 1
                ek += 1
            elif self.comp[i-1] == '=':
                self.table[i][ak] = 1
                ak += 1
            elif self.comp[i-1] == '>=':
                self.table[i][ek] = -1
                self.table[i][ak] = 1
                ek += 1
                ak += 1
         
        M = 10000000
        add = []
        for i in range(1,len(self.table)):
            for j in range(self.nb_vari+self.nb_basi,self.nb_vari+self.nb_basi+self.nb_arti):
                if self.table[i][j] == 1:
                    L1 = self.table[i].copy()
                    L2 = [-i*M for i in L1]
                    L2[j] = 0
                    add.append(L2)
        for j in range(len(self.table[0])):
            for k in add:
                self.table[0][j] += k[j]
        
        columns = []
        for i in range(len(self.table[0])):
            L = []
            for j in range(len(self.table)):
                L.append(self.table[j][i])
            columns.append(L)
        for k in range(len(columns)-2):
            if columns[k].count(0) == len(columns[k])-1:
                self.bas.append(self.all_vari[k])
        for i in self.all_vari:
            if i not in self.bas:
                self.non_bas.append(i)
                    
    def choose_pivot(self):
        coeff = [self.table[0][i] for i in range(len(self.table[0])-2)]
        index2 = self.table[0].index(min(coeff))
        div1 = [None]
        div2 = [None]
        for i in range(1,len(self.table)):
            if self.table[i][index2] != 0:
                n = self.table[i][len(self.table[i])-1]/self.table[i][index2]
            else:
                n = None
            div1.append(n)
            if i not in self.lines_taken:
                div2.append(n)
        div3 = [i for i in div2 if i is not None]
        if div3 == len(div3)*[None]:
            index1 = 999
        else:
            index1 = div1.index(min(div3))
        self.pivot = [index1,index2]
        
    def permute(self,i,j):
        M = []
        M.append(self.bas[i-1])
        M.append(self.all_vari[j])
        for k in range(len(self.non_bas)):
            if self.non_bas[k] == M[0]:
                self.non_bas[k] = M[1]
            elif self.non_bas[k] == M[1]:
                self.non_bas[k] = M[0]
        for k in range(len(self.bas)):
            if self.bas[k] == M[0]:
                self.bas[k] = M[1]
            elif self.bas[k] == M[1]:
                self.bas[k] = M[0]  

    def transform(self):
        self.choose_pivot()
        if 999 not in self.pivot:
            i = self.pivot[0]
            j = self.pivot[1]
            nb = self.table[i][j]
            for k in range(len(self.table[i])):
                self.table[i][k] = self.table[i][k]/nb
            for l in range(len(self.table)):
                value = -1*self.table[l][j]
                if l == i:
                    pass
                else:
                    for m in range(len(self.table[l])):
                        self.table[l][m] = self.table[l][m] + value*self.table[i][m]
            self.lines_taken.append(i)
            self.permute(i,j)
        
    def loop(self):
        self.column = self.all_vari
        self.column.extend(['Z','b'])
        self.index = [f'l{i}' for i in range(1,self.nb_con +1)]
        self.index.insert(0,'Z')
        for i in range(self.nb_con):
            if min(self.table[0]) < 0:
                table = pd.DataFrame(self.table)
                table.columns = self.column
                table.index = self.index
                print("-----------------------------------------------")
                print(table)
                self.transform()
        
def proceed(vari,func,con,method): 
    table1 = tables(vari,func,con,method)
    table1.loop()
    basi = [f'e{i}' for i in range(0,len(con))]
    bas = table1.bas
    non_bas = table1.non_bas
    return vari, basi, non_bas, bas, table1.table

def values(vari, basi, non_bas, bas, T, method):
    Z = T[0][len(T[0])-1]
    R = len(vari)*[0]
    for i in range(len(vari)):
        if vari[i] in non_bas:
            R[i] = 0
        else:
            j = bas.index(vari[i]) + 1
            R[i] = T[j][len(T[j])-1]
    if method == 'mini':
        Z = -Z
    return Z, R

def affiche(vari,Z,R,method):
    if method == 'mini':
        m ='minimum'
    elif method == 'maxi':
        m = 'maximum'
    print()
    print("-----------------------------------------------")
    print("\033[4mResults\033[0m")
    print()
    print(f'The {m} value is F = {Z} with :')
    for i in range(len(vari)):
        print(f'{vari[i]} = {R[i]}')
    
def simplex(vari,func,con,method):
    vari, basi, var, bas, T = proceed(vari,func,con,method)
    Z, R = values(vari, basi, var, bas, T,method)
    affiche(vari, Z, R,method)
    
