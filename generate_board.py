from dfs_jump import *
import chess
import random

def generate_board(Knight_row=-1,Knight_col=-1,PawnNum=5):
    '''
    :param Knight_row: starts from line 1 to line 8
    :param Knight_col: starts from line a to line h
    :param PawnNum: number of black pawns to be eaten.
    :return: a possible board
    '''
    fen='8/8/8/8/8/8/8/8'

    # generate Knight position
    if(Knight_col<=0 or Knight_row<=0 or Knight_row>8 or Knight_col>8):
        print('missing white knight params. Randomly initializing: ')
        Knight_col=random.randint(1,8)
        Knight_row=random.randint(1,8)
    tmp = fen.split('/')
    if(Knight_col==1):
        tmp[8-Knight_row]='N7'
    elif(Knight_col==8):
        tmp[8-Knight_row]='7N'
    else:
        tmp[8-Knight_row]=str(Knight_col-1)+'N'+str(8-Knight_col)

    # generate pawn position


    # change fen according to current board
    fen=''
    for i in range(len(tmp)-1):
        fen+=tmp[i]+'/'
    fen+=tmp[len(tmp)-1]
    board=chess.Board(fen)
    return board
