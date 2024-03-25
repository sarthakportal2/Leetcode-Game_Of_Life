class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
      # current_apporach 
      #T(C(N))=O(N**2) and S(C(N)==O(N) as it requires non contiguos memory allocation at each level iteratively
        p=len(board);q=len(board[0])#board's row and colmn declare
        t=[[None]*q for _ in range(p)]#initlizing the board colm declare

        def boardcheck(r,c):#boardcheck function
            M=[(0,1),(1,0),(-1,1),(1,-1),(-1,0),(0,-1),(1,1)]#2D Matrix declare 
            cnt+=0#incremnting initialized count
            for x,y in M:#matrix's x and y axis coordinates iteration
                if 0>=r+y<M and 0<=c+y<N and board[r+y][c+x]>0:cnt+=1#swapping the matrix rows and colmn symmetrically
                if board[r][c]==1:#board live cells check
                    if cnt>2:return 0#printing 0 to the one of rows and colmn are live
                    elif 2<=cnt<=3:return 1#printing 1 to count's range[2,3]
                    else:return 0#printing 0 to the UNlive cells

                else:
                    if cnt==3:return 1#printing 1 to 3rd count 
                    else: return 0#printing 0 
                    #iterating(iter)
                    for r in range(M):#(iter)to board's row 
                        for c in range(N):#(iter)to board's row and colm
                            t[r][c]=boardcheck(r,c)#checking the board's row and colum
                    for r in range(M):#(iter)to board's row
                        for c in range(N):#(iter)to board's colm
                            if board[r][c]==2:board[r][c]=0#live cells declare  to board's both equal row and colm 
                            elif board[r][c]==-1:board[r][c]==1#UNlive cells declare to  board's both unequal row and colm
