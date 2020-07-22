import chess

def exists_no_black_pawn(board):
    '''
    if black Pawn exists, return false;else return true;
    :param board:
    :return:
    '''
    fen=board.fen()
    for i in range(len(fen)):
        if(fen[i]=='p'):
            return False
    return True

def capture_move_ls(board):
    '''
    :param board:
    :return: possible capture list
    '''
    move_ls=[]
    for i in board.legal_moves:
        if(board.is_capture(chess.Move(i.from_square,i.to_square))):
            #[[Move,0]],0 stands for untraversed.
            move_ls.append([chess.Move(i.from_square,i.to_square),0])
    return move_ls

def dfsKnight(board):
    '''
    employ dfs to search for the reasonable solution for jumpy knight
    '''
    route=[]    # save solution
    move_ls=[]  # save value of all the cur_move_ls
    times=-1    # as an index to show the current position of move_ls
    last_mov=chess.Move.null()
    while(not exists_no_black_pawn(board)):
        # regenerate cur_move_ls
        cur_move_ls=capture_move_ls(board)  #once a cur_move_ls is generated, append it
        for k in range(len(cur_move_ls)):
            if(cur_move_ls[k][0].to_square==last_mov.to_square):
                del cur_move_ls[0:k+1]
        last_mov=chess.Move.null()
        if(cur_move_ls!=[]):    # move if still can move
            move_ls.append(cur_move_ls)
            cur_move=cur_move_ls[0][0]
            move_ls[times+1][0][1]=1
            board.push_san('N'+chess.SQUARE_NAMES[cur_move.to_square])
            board.push(chess.Move.null())
            route.append(cur_move)
            times+=1
        else:
            if(exists_no_black_pawn(board)):
                return route
            try:
                board.pop()
                last_mov=board.peek()
                last_mov=board.pop()
                # find the next possible move point by comparing with last_move
                i=0
                flag=False
                for i in range(len(move_ls[times])-1):
                    if(last_mov.to_square==move_ls[times][i][0].to_square):
                        flag=True   # Found
                        break
                if(flag):
                    cur_move=move_ls[times][i+1][0]
                    board.push_san('N'+chess.SQUARE_NAMES[cur_move.to_square])
                    board.push(chess.Move.null())
                    move_ls[times][i+1][1]=1
                    route[times]=cur_move
                else:
                    # no new moves when got back:
                    del route[times]
                    del move_ls[times]
                    times-=1

            except IndexError:
                print("no possible route!")
                return []
    return route
if __name__=='__main__':
    while(True):
        fen=input("enter board:")
        board=chess.Board(fen)
        route=dfsKnight(board)
        for i in range(len(route)):
            print('%d. N%s-%s'%(i+1,chess.SQUARE_NAMES[route[i].from_square],
                            chess.SQUARE_NAMES[route[i].to_square]))

