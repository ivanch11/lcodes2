class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        Stack<Integer> stack = new Stack <>();
        int[] res = new int[n];
        String[] s = logs.get(0).split(":");
        stack.push(Integer.parseInt(s[0]));
        
        int prev = Integer.parseInt(s[2]);
        for (int i = 1; i<logs.size();i++){
            s = logs.get(i).split(":");
            // while(time<Integer.parseInt(s[2])){
            //     res[stack.peek()]++;
            //     time++;
            // }
            if (s[1].equals("start")){
                if (!stack.isEmpty())
                    res[stack.peek()] += Integer.parseInt(s[2]) - prev;
                stack.push(Integer.parseInt(s[0]));
                prev = Integer.parseInt(s[2]);
            }else{
                res[stack.peek()] += Integer.parseInt(s[2]) - prev + 1;
                stack.pop();
                prev = Integer.parseInt(s[2]) + 1;
            }
        }
        
        
        
        
        return res;
    }
}