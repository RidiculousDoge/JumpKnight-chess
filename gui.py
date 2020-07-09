from tkinter import *
import time
import chess


class BoardGUI:
    mousePressedX=0
    mousePressedY=0
    mouseReleasedX=0
    mouseReleasedY=0

    move2compare=[]

    def __init__(self):
        self.root=Tk()

        self.canvas_width= 800
        self.canvas_height=800

        self.square_size=80

        self.myContainer1=Frame(self.root)
        self.myContainer1.pack()

        # create a canvas
        self.w=Canvas(self.myContainer1,width=self.canvas_width,height=self.canvas_height)
        self.w.pack()

        for i in range(8):
            for j in range(8):
                if((j+1)%2==0):
                    self.w.create_rectangle(i*self.square_size,j*self.square_size,
                                            self.square_size*(i+1),self.square_size*(j+1),fill='grey')
                else:
                    self.w.create_rectangle(i*self.square_size,j*self.square_size,
                                             self.square_size*(i+1),self.square_size*(j+1),fill='darkgreen')

        # update the GUI every 10ms
        self.root.after(10,self.drawPieces)
        self.root.mainloop()

    def Mousepress(self,event):
        self.mousePressedX=int(event.y/self.square_size)
        self.mousePressedY=int(event.x/self.square_size)
        return
    def Mousereleased(self,event):
        self.mouseReleasedX=event.y
        self.mouseReleasedY=event.x
        self.move2compare=[]

        # append the position of the mouse clicked and the mouse released location
        self.move2compare.append((self.mousePressedX, self.mousePressedY, int(self.mouseReleasedX / self.square_size),
                                  int(self.mouseReleasedY / self.square_size)))
        # calls the function determinePiece() from the board.py
        board.Board().determinePiece(self.move2compare)
        # this calls back the function drawPieces() after 100 miliseconds
        self.root.after(100, self.drawPieces())
        return
