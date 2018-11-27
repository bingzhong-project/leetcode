class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i < dp.length; i++) {
            dp[i] = Integer.MAX_VALUE;
            int j = 1;
            while (i >= j * j) {
                if (i == j * j) {
                    dp[i] = 1;
                    break;
                }
                dp[i] = Math.min(dp[i], dp[i - j * j] + dp[j * j]);

                j++;
            }
        }
        return dp[n];
    }
}