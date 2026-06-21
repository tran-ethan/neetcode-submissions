class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        unordered_map<int, int> hashmap;
        int longest = 0;
        for (int n : nums) {
            if (hashmap.contains(n - 1)) {
                hashmap[n] = hashmap[n - 1];
            } else {
                // previous number in the sequence DNE, so start a new sequence
                hashmap[n] = n;
            }
            // Check maximum
            longest = std::max(longest, n - hashmap[n] + 1);
        }
        return longest;
    }
};
