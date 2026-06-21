class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numbers;
        int longest = 0;
        
        for (int n : nums) {
            numbers.insert(n);
        }

        for (int n : nums) {
            if (numbers.contains(n - 1)) {
                continue; // not start of a sequence
            }

            // If here, then it is the start of a sequence
            int seq = n + 1;
            while (numbers.contains(seq)) {
                seq++;
            }
            longest = max(longest, seq - n);
        }
        return longest;
    }
};
