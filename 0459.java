class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int l = s.length();
        for (int i = l/2;i>=1;i--){
            if(l%i==0){
                String subs = s.substring(0,i);
                StringBuilder sb = new StringBuilder();
                
                for (int m = l/i; m>0;m--){
                    sb.append(subs);
                }
                if(sb.toString().equals(s)) return true;
            }
        }
        return false;
    }
}