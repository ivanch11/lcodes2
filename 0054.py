class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        res = []
        rowMin = 0
        rowMax = len(matrix) - 1
        colMin = 0
        colMax = len(matrix[0]) - 1
        while rowMin<=rowMax and colMin<=colMax:

            #if colMin<=colMax:
            for c in range(colMin,colMax + 1,1):
                
                res += [matrix[rowMin][c]]
                
            rowMin += 1                
            #if rowMin<=rowMax:
                #print ("rowMin : ", rowMin)
                #print ("rowMax : ", rowMax)
            for r in range(rowMin,rowMax + 1,1):
                res += [matrix[r][colMax]]

            colMax -= 1
            if rowMin<=rowMax:
                print("colMax: ", colMax)
                print("colMin - 1: ", colMin - 1)
                for c in range(colMax,colMin - 1,-1):
                    print ("res: ", res)
                    res += [matrix[rowMax][c]]
                    print ("res2: ", res)
                rowMax -= 1
            if colMin<=colMax:
                for r in range(rowMax,rowMin - 1,-1):
                    res += [matrix[r][colMin]]
                colMin += 1 
        return res