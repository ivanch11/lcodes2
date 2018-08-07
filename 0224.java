class Solution {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack();
        int sign = 1, result = 0;
        for (int i = 0; i < s.length(); i++){
            if (Character.isDigit(s.charAt(i))){
                int sum = s.charAt(i) - '0';
                while (i+1<s.length() && Character.isDigit(s.charAt(i+1))){
                    sum = 10*sum + s.charAt(++i) - '0';
                }
                result += sign*sum;
            }else if (s.charAt(i) == '+'){
                sign = 1;
            }else if (s.charAt(i) == '-'){
                sign = -1;
            }else if (s.charAt(i) == '('){
                stack.push(result);
                stack.push(sign);
                result = 0;
                sign = 1;
            }else if (s.charAt(i) == ')'){
                result = result*stack.pop()+stack.pop();
            }
                
        }
        return result;
        
    }
}