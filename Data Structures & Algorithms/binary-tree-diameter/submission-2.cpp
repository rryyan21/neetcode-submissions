/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int bestDia = 0;
    
    int diameterOfBinaryTree(TreeNode* root) {
        depth(root);
        return bestDia;
    }

    int depth(TreeNode* root){
        if(root == nullptr){
            return 0;
        }

        int leftDepth = depth(root->left);
        int rightDepth = depth(root->right);

        int currDia = leftDepth + rightDepth;
        if(currDia > bestDia){
            bestDia = currDia;
        }
        return max(depth(root->left), depth(root->right))+1;
    }
};
