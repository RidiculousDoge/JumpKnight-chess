import chess

def exists_no_black_pawn(board):
    # 若有黑兵存在，返回false,否则返回true
    fen=board.fen()
    for i in range(len(fen)):
        if(fen[i]=='p'):
            return False
    return True

def capture_move_ls(board):
    move_ls=[]
    for i in board.legal_moves:
        if(board.is_capture(chess.Move(i.from_square,i.to_square))):
            #[[Move,0]],0表示未被遍历过
            move_ls.append([chess.Move(i.from_square,i.to_square),0])
    return move_ls

def dfsKnight(board):
    '''
    employ dfs to search for the reasonable solution for jumpy knight
    '''
    route=[]    #保存哈密顿道路
    move_ls=[]  #保存所有的cur_move_ls的值
    times=-1     #作为index指示move_ls的当前位置
    last_mov=chess.Move.null()
    while(not exists_no_black_pawn(board)):
        # 重新按条件生成cur_move_ls
        cur_move_ls=capture_move_ls(board)  #每次生成一个cur_move_ls就append进去
        for k in range(len(cur_move_ls)):
            if(cur_move_ls[k][0].to_square==last_mov.to_square):
                del cur_move_ls[0:k+1]
        last_mov=chess.Move.null()
        if(cur_move_ls!=[]):    #如果还可以往前走，就往前走
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
                #通过与last_mov比对的方法找到下一个可能的移动点
                i=0
                flag=False
                for i in range(len(move_ls[times])-1):
                    if(last_mov.to_square==move_ls[times][i][0].to_square):
                        flag=True   #找到了
                        break
                if(flag):
                    cur_move=move_ls[times][i+1][0]
                    board.push_san('N'+chess.SQUARE_NAMES[cur_move.to_square])
                    board.push(chess.Move.null())
                    move_ls[times][i+1][1]=1
                    route[times]=cur_move
                else:
                    # 往前退一步，根本没有新着法，说明这个不对
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

