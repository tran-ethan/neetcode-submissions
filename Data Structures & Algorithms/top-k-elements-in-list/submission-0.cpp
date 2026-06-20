class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> buckets(nums.size() + 1);
        
        for (int n : nums) {
            count[n]++;
        }

        for (const auto& [num, count] : count) {
            buckets[count].push_back(num);
        }

        vector<int> result;

        for (int i = buckets.size() - 1; i > 0; i--) {
            vector<int> bucket = buckets[i];

            for (int n : bucket) {
                result.push_back(n);
                if (result.size() >= k) {
                    break;
                }
            }
            if (result.size() >= k) {
                break;
            }
        }
        return result;
    }
};
