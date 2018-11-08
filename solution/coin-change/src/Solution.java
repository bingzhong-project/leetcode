class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        for(int i = 1; i < dp.length; i++) {
            dp[i] = -1;
        }
        for(int i = 1; i < amount + 1; i++) {
            for(int coin : coins) {
                if(coin <= i && dp[i - coin] != -1) {
                    if(dp[i] != -1) {
                        dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                    } else {
                        dp[i] = dp[i - coin] + 1;
                    }
                } 
            }
        }
        
        return dp[amount];
    }
}