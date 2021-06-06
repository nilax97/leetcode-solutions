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
    TreeNode* bstToGst(TreeNode* root)
    {   
        if(root->right != NULL)
        {
            root->val += sum(root->right);
            bstToGst(root->right);
        }
        if(root->left != NULL)
        {
            bstToGst(root->left);
            root->left = update(root->left, root->val);
        }
        return root;
    }
    
    int sum(TreeNode* root)
    {
        if(root==NULL)
            return 0;
        return root->val + sum(root->left) + sum(root->right);
    }
    
    TreeNode* update(TreeNode* root, int value)
    {
        root->val += value;
        if(root->left != NULL)
            root->left = update(root->left, value);
        if(root->right != NULL)
            root->right = update(root->right, value);
        return root;
    }
};
