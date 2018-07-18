class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(res, 0, s, "")
        return res
    
    def dfs(self, res, level, s, path):
        if level == 4:          

            if not s:
                print ("res.append(path[:-1])")
                res.append(path[:-1])
            return
        
        for i in range (3):
            if i < len(s):
                if i == 0:
                    self.dfs(res, level + 1, s[i+1:], path+s[:i+1]+".")
                elif i == 1 and s[0] != "0":
                    self.dfs(res, level + 1, s[i+1:], path+s[:i+1]+".")
                elif i == 2 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(res, level + 1, s[i+1:], path+s[:i+1]+".")