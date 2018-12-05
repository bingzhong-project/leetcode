class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for (int i = 1; i < nums.length; i++) {
            int[] newNums = new int[nums.length];
            for (int n = 0; n < nums.length; n++) {
                int newLocation = n - i;
                if (newLocation < 0) {
                    newLocation = nums.length + newLocation;
                }
                newNums[newLocation] = nums[n];
            }
            for (int j = 0; j < nums.length; j++) {
                int sum = nums[j] + newNums[j];
                if (sum == target) {
                    result[0] = j;
                    result[1] = (j + i) % nums.length;
                    return result;
                }
            }
        }

        return result;
    }
}