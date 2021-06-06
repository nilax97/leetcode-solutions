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
    int rangeSumBST(TreeNode* root, int L, int R) {
        if(root == NULL)
            return 0;
        int sum = 0;
        if(root->val < L)
        {
            sum = rangeSumBST(root->right, L, R);
        }
        else if(root->val > R)
        {
            sum = rangeSumBST(root->left, L, R);
        }
        else
        {
            sum = root->val + rangeSumBST(root->left, L, R) + rangeSumBST(root->right, L, R);
        }
        return sum;
    }
};
