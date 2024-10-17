import tkinter as Tk
from tkinter.ttk import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import Canvas
import pathlib, os


class mainscreenCls():
    def __init__(self,welComeScreenP):   
        self.welComeScreenP = welComeScreenP
        fontObj=tkFont.Font(size=28,weight="bold",family="Georgia")
        fontObj1=tkFont.Font(size=28,weight="bold",family="Comic Sans MS")
        s=Tk.Label(welComeScreenP,text="PES PLAY ARENA",height=5,font=fontObj)
        t=Tk.Label(welComeScreenP,text="TIC-TAC-TOE",font=fontObj1)

        s.place(x=100,y=500)
        t.place(relx=1,rely=0.5,anchor='center')
        s.pack()
        t.pack(anchor="center") 
        welComeScreenP.attributes('-fullscreen',True)
        button_start=Tk.Button(welComeScreenP,text='Enter Game',width=25,bd =5,highlightbackground = "black",command=self.command_start_button)
        button_start.pack()
        button_start.place(x=930,y=500)
        exit_button=Tk.Button(welComeScreenP,text='Exit',width=25, bd =5,command=welComeScreenP.destroy)
        exit_button.pack()
        exit_button.place(x=150, y=500)
    
    def command_start_button(self):
        obj2 = playScreen(self.welComeScreenP)

class playScreen:
    def __init__(self, welComeScreenP):
        tictacscreen=Tk.Toplevel(welComeScreenP)        
        width=300  
        height=300 
        tictacscreen.geometry('%dx%d+%d+%d' % (300, 300, 450, 200))
        tictacscreen.resizable(0,0)
        tictacscreen.title("Tic tac toe")
        self.tic_tac_button_value = [[2,3,4],[5,6,7],[8,9,10]]
        self.no_of_click = 1
        """cross_img = "Cross.png"
        cross_img_path = os.path.join(current_dir, cross_img)"""
        photo_cross = Tk.PhotoImage(file=r"D:\Cross.png") 
        self.resized_photo_cross =photo_cross.subsample(2,2)   
        """circle_img = "circle.png"
        circle_img_path = os.path.join(current_dir, circle_img) """
        photo_zero = Tk.PhotoImage(file=r"D:\circle_2.png")  
        self.resized_photo_zero =photo_zero.subsample(2,2) 
        self.intializationButton(tictacscreen)
        self.drawLine(tictacscreen)
    
    def intializationButton(self,tictacscreen):
        tic_tac_toe_button = [[0,0,0],[0,0,0],[0,0,0]] 
        self.tic_tac_toe_button =tic_tac_toe_button   
        tic_tac_toe_button[0][0]=Tk.Button(tictacscreen,text="1",width="100",height="100",bd =5 ,fg='black',highlightbackground = "black",highlightthickness = 2,command=lambda:self.on_button_click(0,0))
        tic_tac_toe_button[0][0].pack()    
        tic_tac_toe_button[0][0].place(x=0,y=0)
        tic_tac_toe_button[0][1]=Tk.Button(tictacscreen,text="2",width="100",height="100",bd =5 ,fg='black',command=lambda:self.on_button_click(0,1))
        tic_tac_toe_button[0][1].pack()
        tic_tac_toe_button[0][1].place(x=0,y=100)
        tic_tac_toe_button[0][2]=Tk.Button(tictacscreen,text="3",width="100",height="100",bd =5 ,fg='black',command=lambda:self.on_button_click(0,2))
        tic_tac_toe_button[0][2].pack()
        tic_tac_toe_button[0][2].place(x=0,y=200)
        tic_tac_toe_button[1][0]=Tk.Button(tictacscreen,text="4",width="100",height="100",bd =5 ,fg='black',command=lambda:self.on_button_click(1,0))
        tic_tac_toe_button[1][0].pack()
        tic_tac_toe_button[1][0].place(x=100,y=0)
        tic_tac_toe_button[1][1]=Tk.Button(tictacscreen,text="5",width="100",height="100",bd =5 ,fg='black',command=lambda:self.on_button_click(1,1))
        tic_tac_toe_button[1][1].pack()
        tic_tac_toe_button[1][1].place(x=100,y=100)
        tic_tac_toe_button[1][2]=Tk.Button(tictacscreen,text="6",width="100",height="100",bd =5 ,fg='black',command=lambda:self.on_button_click(1,2))
        tic_tac_toe_button[1][2].pack()
        tic_tac_toe_button[1][2].place(x=100,y=200)
        tic_tac_toe_button[2][0]=Tk.Button(tictacscreen,text="7",width="100",height="100",bd =5 ,fg='black',command=lambda:self.on_button_click(2,0))
        tic_tac_toe_button[2][0].pack()
        tic_tac_toe_button[2][0].place(x=200,y=0)
        tic_tac_toe_button[2][1]=Tk.Button(tictacscreen,text="8",width="100",height="100",bd =5 ,fg='black',command=lambda:self.on_button_click(2,1))
        tic_tac_toe_button[2][1].pack()
        tic_tac_toe_button[2][1].place(x=200,y=100)
        tic_tac_toe_button[2][2]=Tk.Button(tictacscreen,text="9",width="100",height="100",bd =5 ,fg='black',command=lambda:self.on_button_click(2,2))
        tic_tac_toe_button[2][2].pack()
        tic_tac_toe_button[2][2].place(x=200,y=200)

    """def drawline(self,tictacscreen = None):
        self.tictacscreen = tictacscreen
        self.canvas = Canvas(self.tictacscreen)
        self.canvas.create_line(0, 100, 300, 100)
        self.canvas.pack(fill = BOTH, expand = True)"""

    def on_button_click(self,btn_index_x,btn_index_y ):
        print(btn_index_x ,btn_index_y,self.no_of_click) 
        if( self.tic_tac_button_value[btn_index_x][btn_index_y]!=0  and self.tic_tac_button_value[btn_index_x][btn_index_y]!=1) :
            if self.no_of_click%2==0:
                self.tic_tac_toe_button[btn_index_x][btn_index_y].config(image=self.resized_photo_cross)
                self.tic_tac_button_value[btn_index_x][btn_index_y]=1           
            else:
                self.tic_tac_toe_button[btn_index_x][btn_index_y].config(image=self.resized_photo_zero)
                self.tic_tac_button_value[btn_index_x][btn_index_y]=0
            winner_value=self.checkWinner(self.tic_tac_button_value)
            if winner_value==1:
                print("player with cross wins ")
                messagebox.showinfo("Tic Tac Toe","The player with cross is the winner!")
                        
            if winner_value==0:
                print("player w ith 0 wins")
                messagebox.showinfo("Tic Tac Toe","The player with cirlce is the winner!")

            self.no_of_click = self.no_of_click+1
            if self.no_of_click==10:
                messagebox.showinfo("Tic Tac Toe","Its a Draw")


      
    def checkWinner(self,tic_tac_toe_button_value):
        win_value =2
        iSWinner = False
        print(tic_tac_toe_button_value)
        if (tic_tac_toe_button_value[0][0] == tic_tac_toe_button_value[0][1] == tic_tac_toe_button_value[0][2]) :
            win_value = tic_tac_toe_button_value[0][0]
            iSWinner = True
        if (tic_tac_toe_button_value[1][0] == tic_tac_toe_button_value[1][1] == tic_tac_toe_button_value[1][2]) :
            win_value = tic_tac_toe_button_value[1][0]
            iSWinner = True
        if (tic_tac_toe_button_value[2][0] == tic_tac_toe_button_value[2][1] == tic_tac_toe_button_value[2][2]) :
            win_value = tic_tac_toe_button_value[2][0]
            iSWinner = True
        if (tic_tac_toe_button_value[0][0] == tic_tac_toe_button_value[1][0] == tic_tac_toe_button_value[2][0]) :
            win_value = tic_tac_toe_button_value[0][0]
            iSWinner = True
        if (tic_tac_toe_button_value[0][1] == tic_tac_toe_button_value[1][1] == tic_tac_toe_button_value[2][1]) :
            win_value = tic_tac_toe_button_value[1][0]
            iSWinner = True
        if (tic_tac_toe_button_value[0][2] == tic_tac_toe_button_value[1][2] == tic_tac_toe_button_value[2][2]) :
            win_value = tic_tac_toe_button_value[2][0]
            iSWinner = True
        if (tic_tac_toe_button_value[0][0] == tic_tac_toe_button_value[1][1] == tic_tac_toe_button_value[2][2]) :
            win_value = tic_tac_toe_button_value[0][0]
            iSWinner = True
        if (tic_tac_toe_button_value[0][2] == tic_tac_toe_button_value[1][1] == tic_tac_toe_button_value[2][0]) :
            win_value = tic_tac_toe_button_value[0][2]
            iSWinner = True
        if (iSWinner):
            return win_value 
        return win_value

welComeScreen=Tk.Tk()

current_dir = pathlib.Path(__file__).parent.resolve()
tictac_img = "tictactoe_pic.png"
tictac_img_path = os.path.join(current_dir, tictac_img)
img = Tk.PhotoImage(file=r"D:\tictactoe_pic.png")
imglabel=Label(welComeScreen,image=img, width= 10)
imglabel.pack()
imglabel.place(x=500,y=300)
welComeScreen.title("TIC-TAC-TOE")
welComeScreen.geometry("500x250")
cls = mainscreenCls(welComeScreen)
welComeScreen.mainloop()   