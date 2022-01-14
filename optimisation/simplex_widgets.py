import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
                             qApp , QMainWindow,QApplication, QMainWindow, 
                             QWidget, QRadioButton, QLabel, QGridLayout,
                             QComboBox)
import bigM

class Home(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Home')
        self.l0 = QLabel("Welcome to my simplex maximization program")
        self.l1 = QLabel("Pleae choose what you want to run : ")
        self.ch1 = QRadioButton("Manual input")
        self.ch2 = QRadioButton("Use presets")
        self.beg = QPushButton("Begin")
        self.space = QLabel()
        self.init_ui()
        
        
    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.l0)
        v_box.addWidget(self.space)
        v_box.addWidget(self.l1)
        v_box.addWidget(self.ch1)
        v_box.addWidget(self.ch2)
        v_box.addWidget(self.space)
        v_box.addWidget(self.beg)
        
        self.setLayout(v_box)
        self.show()
        
        self.beg.clicked.connect(self.begin)
        
    def begin(self):
        if self.ch1.isChecked():
            self.choice = Choice()
            self.choice.show()
            self.close()
        if self.ch2.isChecked():
            self.question = Questions()
            self.question.show()
            self.close()
        
class Questions(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Presets')
        self.l1 = QLabel("You can choose between these 3 examples : ")
        self.Q1 = QRadioButton("Question 1")
        self.Q2 = QRadioButton("Question 2")
        self.Q3 = QRadioButton("Question 3")
        self.space = QLabel()
        self.b_exec = QPushButton('Continue')
        
        self.init_ui()
        self.show()
    
    def init_ui(self):
        
        v_box = QVBoxLayout()
        v_box.addWidget(self.l1)
        v_box.addWidget(self.Q1)
        v_box.addWidget(self.Q2)
        v_box.addWidget(self.Q3)
        v_box.addWidget(self.space)
        v_box.addWidget(self.b_exec)
        
        self.setLayout(v_box)
        self.b_exec.clicked.connect(self.execute)
    
    def execute(self):
        if self.Q1.isChecked():
            vari = ['x1','x2','x3']
            func = [11,16,15]
            con = [[1,2,3/2,12000],
                   [2/3,2/3,1,4600],
                   [1/2,1/3,1/2,2400],
                   ['<=','<=','<=']
                   ]
            method = 'maxi'
        elif self.Q2.isChecked():
            vari = ['x1','x2']
            func = [20000,25000]
            con = [[400,300,25000],
                   [300,400,27000],
                   [200,500,30000],
                   ['>=','>=','>=']
                   ]
            method = 'mini'
        elif self.Q3.isChecked():
            vari = ['x1','x2','x3','x4']
            func = [30,36,25,30]
            con = [[1,1,0,0,200],
                   [0,0,1,1,300],
                   [1,0,1,0,400],
                   [0,1,0,1,300],
                   ['=','=','<=','<=']
                   ]
            method = 'mini'
        self.table = Table(len(vari),len(con)-1,method)
        self.table.presets(vari,func,con)
        self.table.show()
        
class Choice(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Parameters')
        self.l0 = QLabel("What is your system like ?")
        self.mini = QRadioButton("Minimisation")
        self.maxi = QRadioButton("Maximisation")
        self.l_var = QLabel('Number of variables : ')
        self.var = QLineEdit()
        self.l_con = QLabel("Number of constrincts : ")
        self.con = QLineEdit()
        self.space = QLabel()
        self.b_exec = QPushButton('Continue')
        
        self.init_ui()
        self.show()
        
    def init_ui(self):
        h_box1 = QHBoxLayout()
        h_box1.addWidget(self.l_var)
        h_box1.addWidget(self.var)
        
        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.l_con)
        h_box2.addWidget(self.con)
        
        v_box = QVBoxLayout()
        v_box.addWidget(self.l0)
        v_box.addWidget(self.maxi)
        v_box.addWidget(self.mini)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.space)
        v_box.addWidget(self.b_exec)
        
        self.setLayout(v_box)
        self.b_exec.clicked.connect(self.continu)
    
    def continu(self):
        self.nb_var = int(self.var.text())
        self.nb_con = int(self.con.text())
        if self.mini.isChecked():
            self.choice = 'mini'
        elif self.maxi.isChecked():
            self.choice = 'maxi'
        self.table = Table(self.nb_var,self.nb_con,self.choice)
        self.table.show()

class Table(QWidget):
    
    def __init__(self,nb_var,nb_con,choice):
        super().__init__()
        self.nb_var = nb_var
        self.nb_con = nb_con
        self.choice = choice
        if self.choice == 'mini':
            self.title = 'minimisation'
        elif self.choice == 'maxi':
            self.title = 'maximisation'
        self.setWindowTitle(f'Initial table : {self.title}')
        self.space = QLabel()
        
        self.x = [f'x{i}' for i in range(nb_var)]
        self.T = [{}]
        for i in range(nb_con):
            self.T.append({})
        for i in range(nb_var):
            self.T[0][self.x[i]] = QLineEdit()
            for k in range(1,nb_con+1):
                self.T[k][self.x[i]] = QLineEdit()
                self.T[k]['s'] = QComboBox()
                self.T[k]['s'].addItems(['<=','=','>='])
                self.T[k]['b'] = QLineEdit()
            
        self.b_exec = QPushButton("Compute")
        self.init_ui()
        self.show()
        
    def init_ui(self):
        v_box = QVBoxLayout()
        for i in range(len(self.T)):
            h_box = QHBoxLayout()
            if i == 0:
                h_box.addWidget(QLabel("Z = "))
            for j in range(self.nb_var - 1):
                h_box.addWidget(self.T[i][f'x{j}'])
                h_box.addWidget(QLabel(f'{self.x[j]} + '))
            h_box.addWidget(self.T[i][f'x{self.nb_var -1}'])
            h_box.addWidget(QLabel(f'{self.x[self.nb_var -1]}'))
            if i!= 0:
                h_box.addWidget(self.T[i]['s'])
                h_box.addWidget(self.T[i]['b'])
            v_box.addLayout(h_box)
        v_box.addWidget(self.space)
        v_box.addWidget(self.b_exec)
        
        self.setLayout(v_box)
        self.b_exec.clicked.connect(self.compute)
    
    def compute(self):
        self.vari = self.x
        self.func = [int(self.T[0][f'x{j}'].text()) for j in range(self.nb_var)]
        self.con = []
        for i in range(1,self.nb_con+1):
            L1 = [float(self.T[i][f'x{j}'].text()) for j in range(self.nb_var)]
            L1.append(float(self.T[i]['b'].text()))
            self.con.append(L1)
        L2 = [self.T[i]['s'].currentText() for i in range(1,self.nb_con+1)]
        self.con.append(L2)
        bigM.simplex(self.vari,self.func,self.con,self.choice)
    
    def presets(self,vari,func,con):
        for j in range(len(vari)):
            self.T[0][f'x{j}'].setText(str(func[j]))
        for i in range(len(con)-1):
            for j in range(len(vari)):
                self.T[i+1][f'x{j}'].setText(str(con[i][j]))
            self.T[i+1]['b'].setText(str(con[i][len(con[i])-1]))
            self.T[i+1]['s'].setCurrentIndex(['<=','=','>='].index(con[len(con)-1][i]))
                
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Home()
    sys.exit(app.exec_())  