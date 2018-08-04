class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int diff = Integer.MAX_VALUE;
        int optSum = nums[0]+nums[1]+nums[2];
        Arrays.sort(nums);
        for (int i = 0; i<nums.length-2;i++ ){
            int second = i + 1;
            int last = nums.length-1;
            while (second<last){
                int curSum = nums[i]+nums[second]+nums[last];
                if (curSum > target)
                    last--;         
                else if (curSum < target)
                    second++;
                else
                    return curSum;
                if (Math.abs(curSum-target)<Math.abs(optSum-target))
                    optSum = curSum;
            }

            
        }
        return optSum;
    }
}