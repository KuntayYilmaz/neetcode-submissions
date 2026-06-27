class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        int n = strs[0].size();
        for(int i = 0;i < n;i++)
        {
            for(const string& s : strs)
            {
                if(i == s.size() || strs[0][i] != s[i])
                {
                    return s.substr(0,i);
                }
            }
        } 
        return strs[0];   
    }
};