class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length()>s2.length()) return false;
        //int i = 0;
        int[] map1 = new int[26];
        int[] map2 = new int[26];
        for (int j = 0; j<s1.length(); j++){
            map1[s1.charAt(j)-'a']++;
            map2[s2.charAt(j)-'a']++;
        }
        for (int j = 0; j+s1.length()<s2.length(); j++){
            if (match(map1, map2)) return true;
            map2[s2.charAt(j)-'a']--;
            map2[s2.charAt(j+s1.length())-'a']++;
        }
        return match(map1, map2);
    }
    
    private boolean match(int[] map1, int[] map2){
        for (int i = 0; i<map1.length;i++){
            if (map1[i] != map2[i])
                return false;
        }
        return true;
    }
}