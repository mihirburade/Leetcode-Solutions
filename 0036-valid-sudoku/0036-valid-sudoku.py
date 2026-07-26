class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # def valid(board):
        
        
            #for rows
        for rows in range(0,9):
            seen=set()
            for col in range(0,9):
                value=board[rows][col]
                if value in seen:
                    # print("not valid -rows")
                    return False
                if value==".":
                    continue
                # if value not in seen:
                seen.add(value)
        #for col
        for col in range(0,9):
            seen=set()
            for row in range(0,9):
                value=board[row][col]
                if value in seen:
                    # print("not valid -colums")
                    return False
                if value==".":
                    continue
                # if value not in seen:
                seen.add(value)
        #for box
        for row_box in range(0,9,3):
                for col_box in range(0,9,3):
                    seen=set()    
                    for i in range(3):
                        for j in range(3):
                        
                            value=board[row_box+i][col_box+j]
                            if value in seen:
                                # print("not valid-box")
                                return False
                            if value==".":
                                continue
                            # if value not in seen:
                            seen.add(value)
        return True
        # return(valid(board))
