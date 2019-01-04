import java.util.Arrays;

class Solution {
    public boolean makesquare(int[] nums) {
        if (nums.length < 4) {
            return false;
        }
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 4 != 0) {
            return false;
        }
        int target = (int) (sum / 4);
        int[] sides = { target, target, target, target };
        Arrays.sort(nums);
        return dfs(nums, sides, 0);
    }

    public boolean dfs(int[] nums, int[] sides, int index) {
        if (index == nums.length) {
            return true;
        }

        for (int i = 0; i < 4; i++) {
            if (sides[i] - nums[index] < 0) {
                return false;
            }
            sides[i] -= nums[index];
            if (dfs(nums, sides, index + 1)) {
                return true;
            }
            sides[i] += nums[index];
        }

        return false;
    }
}