class Solution {
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) 
            return;
        int insertLoc = 0;
        for (int n : nums)
            if (n != 0)
                nums[insertLoc++] = n;
        while (insertLoc<nums.length)
            nums[insertLoc++] = 0;
    }
}