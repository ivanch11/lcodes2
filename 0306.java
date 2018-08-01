class Solution {
    public boolean isAdditiveNumber(String num) {
        int n = num.length();
        for (int i = 1; i<=n/2 ; i++){
            if (num.charAt(0) == '0' && i >= 2){
                break;
            }
            for (int j = i + 1; n-j>= j-i && n-j >= i; j++){
                if (num.charAt(i) == '0' && j -i>= 2){
                    break;
                }
                long num1 = Long.parseLong(num.substring(0,i));
                long num2 = Long.parseLong(num.substring(i,j));
                String str3 = num.substring(j);
                if (recur(num1, num2, str3)){
                    return true;
                }
            }
        }
        return false;
    }
    
    private boolean recur(long num1, long num2, String str3){
        if (str3.length() == 0){
            return true;
        }
        long sum = num1 + num2;
        String sum_str = Long.toString(sum);
        if (str3.startsWith(sum_str)){
            return recur(num2, sum, str3.substring(sum_str.length()));
        }else{
            return false;
        }
    }
}