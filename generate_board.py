from dfs_jump import *
import chess
import random
from tqdm import trange

def generate_board(knight_row=-1,knight_col=-1,pawnNum=5):
    '''
    :param Knight_row: starts from line 1 to line 8
    :param Knight_col: starts from line a to line h
    :param PawnNum: number of black pawns to be eaten.
    :return: a possible board
    '''
    fen='8/8/8/8/8/8/8/8'
    board=chess.Board(fen)
    # generate Knight position
    if(knight_col<=0 or knight_row<=0 or knight_row>8 or knight_col>8):
        print('missing white knight params. Randomly initializing: ')
        knight_col=random.randint(1,8)
        knight_row=random.randint(1,8)
        
    # set knight:
    knight_num = exchange_to_square_num(knight_row, knight_col)
    knight_piece = chess.Piece(chess.KNIGHT, chess.WHITE)
    board.set_piece_at(knight_num, knight_piece)
    
    while(dfsKnight(board)==[]):
        # generate pawn position
        pawn_num_ls=generate_pawn_ls(knight_num,pawnNum)
    
        # set pawns
        pawn_piece=chess.Piece(chess.PAWN,chess.BLACK)
        for target_num in pawn_num_ls:
            board.set_piece_at(target_num,pawn_piece)

    return board

def generate_pawn_ls(Knight_num,pawnNum):
    '''
    :param Knight_num: current square number of the white knight
    :param pawnNum: numbers of pawn to add
    :return: a possible pawn ls, each position of pawn is represented by square_number
    '''
    pawn_ls=[]
    for i in trange(pawnNum,desc='generating pawn'):
        pawn_row=random.randint(1,8)
        pawn_col=random.randint(1,8)
        square_num=exchange_to_square_num(pawn_row,pawn_col)
        if(square_num!=Knight_num and square_num not in pawn_ls):
            pawn_ls.append(square_num)
        else:
            i-=1
            continue
    return pawn_ls

def exchange_to_square_num(row,col):
    '''
    :param row: row 1 to 8
    :param col: col 1 to 8, representing col a to h
    :return: target square number(0 to 63), where A1=0,B1=1,... H8=63
    '''
    row=int(row)
    col=int(col)
    return (row-1)*8+col-1

if __name__=='__main__':
    board=generate_board(pawnNum=10)
    print(board.fen())
    route=dfsKnight(board)
    showformatRoute(route)



