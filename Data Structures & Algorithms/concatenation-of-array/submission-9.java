class Solution {
    public int[] getConcatenation(int[] nums) {
       int nums2[] = new int[nums.length * 2];
       int n = nums.length;
       for(int i = 0; i < nums.length; i++){
        nums2[i] = nums2[i+n] = nums[i];
       } 
       return nums2;
    }
}