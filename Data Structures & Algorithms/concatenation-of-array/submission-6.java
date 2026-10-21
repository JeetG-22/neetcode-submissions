class Solution {
    public int[] getConcatenation(int[] nums) {
        int nums2[] = new int[nums.length * 2];
        int k = 0;
        for(int i = 0; i < 2; i++){
            for(int j = 0; j < nums.length; j++) {
                nums2[k] = nums[j];
                k++;
            }
        }
        return nums2;
    }
}