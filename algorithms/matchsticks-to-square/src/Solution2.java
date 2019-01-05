import java.util.Arrays;
import java.util.concurrent.atomic.AtomicBoolean;

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
        Arrays.sort(nums);
        AtomicBoolean res = new AtomicBoolean(false);
        boolean[] visited = new boolean[nums.length];
        dfs(res, nums, visited, sum / 4, 0, 0, 0);
        return res.get();
    }

    public void dfs(AtomicBoolean res, int[] nums, boolean[] visited, int target, int sideIndex, int sideSum,
            int index) {
        if (res.get()) {
            return;
        }
        if (sideIndex == 4) {
            res.set(true);
            return;
        }
        if (sideSum == target) {
            dfs(res, nums, visited, target, sideIndex + 1, 0, 0);
        }
        for (int i = index; i < nums.length; i++) {
            if (visited[i]) {
                continue;
            }
            if (nums[i] + sideSum <= target) {
                visited[i] = true;
                dfs(res, nums, visited, target, sideIndex, sideSum + nums[i], i + 1);
                visited[i] = false;
            }
        }
    }
}