#include <vector>
class Solution 
{
public:
    bool hasDuplicate(vector<int>& nums) 
    {
        bool didFound = 0;
        for(int i = 0;i < nums.size();i++)
        {
            for(int j = i+1;j < nums.size();j++)
            {
                if(nums[i] == nums[j])
                {
                    didFound = 1;
                }
            }
        } 
        return didFound;
    }
};
