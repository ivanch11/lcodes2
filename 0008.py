class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        sign = 1
        currentValue = 0
        max_int = 2**31 - 1
        max_int_10 = int(max_int/10)
        min_int = 2**31 
        min_int_10 = int(min_int/10)
        str_length = len(str)
        max_int_last = max_int%10
        min_int_last = min_int%10
        
        if str_length == 0:
            return 0
        for c in str:
            if c == ' ':
                i += 1
            else:
                break
        if str_length - i <= 0:
            return 0
        if str[i] == '-':
            sign = -1        
            i += 1
        elif str[i] == '+':     
            i += 1            
        while i < str_length and str[i] >= '0' and str[i] <= '9':
            int_i = int(str[i])
            if sign == 1:
                if currentValue > max_int_10 or ( currentValue == max_int_10 and int_i > max_int_last):
                    return max_int
            else:
                if currentValue > min_int_10 or ( currentValue == min_int_10 and int_i > min_int_last):
                    return sign*min_int
            currentValue *= 10
            currentValue += int_i
            i += 1

        return sign*currentValue