class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack();
        for (int ast:asteroids){
            colli: {
                while (!stack.isEmpty() && ast < 0 && stack.peek() > 0){
                    if (stack.peek() < -ast){
                        stack.pop();
                        continue;
                    }
                    else if (stack.peek() == -ast){
                        stack.pop();                        
                    }  
                    break colli;
                }
                stack.push(ast);
                
            }
        }
        int[] res = new int[stack.size()];
        for (int i = stack.size()-1; i>=0;i--)
            res[i] = stack.pop();
        return res;
    }
}