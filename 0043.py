class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)        
        res_Int = [0] * (l1 + l2)
        res_str = ""
        for i in range(l1 - 1, -1 , -1):
            for j in range (l2 -1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = p1 + 1
                sum = mul + 10 * res_Int[p1] + res_Int[p2]                
                
                res_Int[p2] = sum % 10
                res_Int[p1] = sum // 10
        print (res_Int)        
        for digi in res_Int:
            print ("digi : ", digi)
            if res_str == "" and digi == 0:
                continue
            res_str += str(digi)
            print ("res_str: ", res_str)
        return "0" if res_str == "" else res_str