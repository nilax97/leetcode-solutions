/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        if(nums.size()==0)
        {
            return NULL;
        }
        int max_i = 0;
        for(int i=1; i<nums.size(); ++i)
        {
            if(nums[i] > nums[max_i])
            {
                max_i = i;
            }
        }
        TreeNode *root = new TreeNode(nums[max_i]);
        vector<int> nums_l(max_i);
        vector<int> nums_r(nums.size() - max_i - 1);
        for(int i=0; i<nums.size(); ++i)
        {
            if(i<max_i)
            {
                nums_l[i] = nums[i];
            }
            else if(i>max_i)
            {
                nums_r[i-max_i-1] = nums[i];
            }
        }
        root->left = constructMaximumBinaryTree(nums_l);
        root->right = constructMaximumBinaryTree(nums_r);
        return root;
    }
};
