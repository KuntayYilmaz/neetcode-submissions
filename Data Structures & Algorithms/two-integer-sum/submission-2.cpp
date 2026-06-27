class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        int n = nums.size();
        unordered_map<int,int> hashmap {};
        for(int i = 0;i < n;i++)
        {
            if(hashmap.contains(target-nums[i]))
            {
                return {hashmap[target-nums[i]],i};
            }
            hashmap[nums[i]] = i;
        }
    }
};
