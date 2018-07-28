class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> r2i = new HashMap<>();
        r2i.put('I',1);
        r2i.put('V',5);
        r2i.put('X',10);
        r2i.put('L',50);
        r2i.put('C',100);
        r2i.put('D',500);
        r2i.put('M',1000);
        //int prev = -1;
        //int prev = r2i.get(s.charAt(s.length()-1));
        int ans = 0;
        for (int i = s.length()-1, prev = -1; i>=0;i--){
            int cur = r2i.get(s.charAt(i));
            if (cur >= prev) 
                ans += cur;
            else
                ans -= cur;
            prev = cur;        
        }
        return ans;
    }
}