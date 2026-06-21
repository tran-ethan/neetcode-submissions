class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numbers(nums.begin(), nums.end());
        int longest = 0;

        for (int n : numbers) {
            // If here, then it is the start of a sequence
            if (!numbers.contains(n - 1)) {
                int seq = 1;
                while (numbers.contains(n + seq)) {
                    seq++;
                }
                longest = max(longest, seq);
            }

        }
        return longest;
    }
};
