from flask import Flask
app = Flask(__name__)

from flask import render_template
import random

class Board(object):
    def __init__(self):
        self.full_board = []
        self.key = 0
        self.board_string = ""
        self.midsum = []
        self.cond = []
        self.flip = 0

    def set_board(self):
        self.full_board = [random.randint(0,1) for i in range(64)]
        self.key = random.randint(0,63)
        self.board_string = ""
        for i in range(64):
            if (i%8==0):
                self.board_string+="   "
            else:
                self.board_string+="        "
            if (self.full_board[i]==0):
                self.board_string+="T"
            else:
                self.board_string+="H"
    
    def get1(self):
        print("HERE:"+self.board_string[0:67])
        return self.board_string[0:67]
    
    def get2(self):
        return self.board_string[67:137]
    
    def get3(self):
        return self.board_string[134:202]
    
    def get4(self):
        return self.board_string[201:269]
    
    def get5(self):
        return self.board_string[268:336]
    
    def get6(self):
        return self.board_string[335:403]
    
    def get7(self):
        return self.board_string[402:470]
    
    def get8(self):
        return self.board_string[469:537]
    
    def setandget1(self):
        self.set_board()
        return self.get2()

    def sum_board(self):
        midsum = [0]*6
        for i in range(64):
            if (i%2==1):
                midsum[0] = (midsum[0]+self.full_board[i])%2
            if (i%4>=2):
                midsum[1] = (midsum[1]+self.full_board[i])%2
            if (i%8>=4): 
                midsum[2] = (midsum[2]+self.full_board[i])%2
            if (i%16>=8): 
                midsum[3] = (midsum[3]+self.full_board[i])%2
            if (i%32>=16):
                midsum[4] = (midsum[4]+self.full_board[i])%2
            if (i>=32):
                midsum[5] = (midsum[5]+self.full_board[i])%2
        self.midsum = midsum
        return '('+str(midsum[0])+', '+str(midsum[1])+', '+str(midsum[2])+', '+str(midsum[3])+', '+str(midsum[4])+', '+str(midsum[5])+')'
    
    def get_cond(self):
        cond = [True]*6
        if (self.midsum[0]==1):
            cond[0] = True
        else:
            cond[0] = False
        if (self.midsum[1]==1):
            cond[1] = True
        else:
            cond[1] = False
        if (self.midsum[2]==1):
            cond[2] = True
        else:
            cond[2] = False
        if (self.midsum[3]==1):
            cond[3] = True
        else:
            cond[3] = False
        if (self.midsum[4]==1):
            cond[4] = True
        else:
            cond[4] = False
        if (self.midsum[5]==1):
            cond[5] = True
        else:
            cond[5] = False
        self.cond = cond
        return cond
    
    def find_square(self, cond):
        for i in range(64):
            if ((i%2==1)==cond[0] and (i%4>=2)==cond[1] and (i%8>=4)==cond[2] and (i%16>=8)==cond[3] and (i%32>=16)==cond[4] and (i>=32)==cond[5]):
                self.flip = i
                return i

    def calc_flip(self):
        new_cond = [(self.key%2==1)!=self.cond[0], (self.key%4>=2)!=self.cond[1], (self.key%8>=4)!= self.cond[2], (self.key%16>=8)!=self.cond[3], (self.key%32>=16)!=self.cond[4], (self.key>=32)!=self.cond[5]]
        return self.find_square(new_cond)
    
    def verify(self):
        self.key = 0
        self.midsum = []
        self.cond = []
        self.full_board[self.flip] = (self.full_board[self.flip]+1)%2
        self.sum_board()
        return self.find_square(self.get_cond())

@app.route('/')
def refresh_board():
    main = Board()
    return render_template('index.html', row_1=main.setandget1(), row_2=main.get2(), row_3=main.get3(), row_4=main.get4(), row_5=main.get5(), row_6=main.get6(), row_7=main.get7(), row_8=main.get8(), square_num = main.key, init_sum=main.sum_board(), init_square=main.find_square(main.get_cond()), last_square=main.calc_flip(), test=main.verify())
