class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        std::vector<int> dp(cost.size());

        for (int i = 0; i < 2; i++) {
            dp[i] = cost[i];
        }

        for (int i = 2; i < dp.size(); i++) {
            dp[i] = std::min(dp[i-1], dp[i - 2]) + cost[i];
        }

        int minimum = std::min(dp[dp.size() - 1], dp[dp.size() - 2]);
        return minimum;
    }
};
