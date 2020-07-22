import pygame
import chess
import time

SIZE=800
WIDTH=800
HEIGHT=600
SQUARE_SIZE=60
Black_color=[0,0,0]
White_color=[255,255,255]

class ChessBoard:
    def __init__(self):
        # 左边部分用来画棋盘，右边部分用来画棋子
        # the board is 600*600
        self.left=600
        self.right=SIZE-self.left
        self.board=chess.Board('8/8/8/8/8/8/8/8')
        self.load_img()
    def reset(self):
        self.board=chess.Board('8/8/8/8/8/8/8/8')
    def load_img(self):
        self.whiteKnight=pygame.image.load('img/knightWhite.gif')
        self.blackKnight=pygame.image.load('img/knightBlack.gif')
        self.whitebishop=pygame.image.load('img/bishopWhite.gif')
        self.blackbishop=pygame.image.load('img/bishopBlack.gif')
        self.whiteRook=pygame.image.load('img/rookWhite.gif')
        self.blackRook=pygame.image.load('img/rookBlack.gif')
        self.whiteQueen=pygame.image.load('img/queenWhite.gif')
        self.blackQueen=pygame.image.load('img/queenBlack.gif')
        self.whiteKing=pygame.image.load('img/kingWhite.gif')
        self.blackKing=pygame.image.load('img/kingBlack.gif')
        self.whitePawn=pygame.image.load('img/pawnWhite.gif')
        self.blackPawn=pygame.image.load('img/pawnBlack.gif')

    def draw(self,screen):
        for h in range(8):
            #竖线
            pygame.draw.line(screen,Black_color,[20+SQUARE_SIZE*h,20],[20+SQUARE_SIZE*h,500])
            #横线
            pygame.draw.line(screen,Black_color,[20,20+SQUARE_SIZE*h],[500,20+SQUARE_SIZE*h])
        fen=self.board.fen().split('/')
        for i in range(len(fen)):
            if()

    '''
    def update(self):
        # 每xxms更新显示self.board
    '''

def get_square_name(event):
    x, y = event.pos
    if (x <= 20 or y <= 20 or y > 500 or (x > 500 and x < 600)):
        pass
    elif (x <= 600):
        # round函数四舍五入
        file_square = int((x - 20) / 60)
        rank_square = int((y - 20) / 60)
        square_name = chess.FILE_NAMES[file_square] + chess.RANK_NAMES[rank_square]
        current_pos = square_name
    elif x>600:
        pass
    return square_name

if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption('跳跳马')
    screen=pygame.display.set_mode((SIZE,SIZE))
    running=True
    gui=ChessBoard()
    gui.draw()
    while running:
        current_pos=''
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.KEYUP:
                pass
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                current_pos=get_square_name(event)
            elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
                square_name=get_square_name(event)
                
    pygame.quit()




