//
// Created by fanwu on 2020/1/1.
//

#ifndef LEECODE_ISVALIDBST_H
#define LEECODE_ISVALIDBST_H

#endif //LEECODE_ISVALIDBST_H

#include <iostream>
#include <climits>

using namespace std;
namespace isValidBST {
    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;

        TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    };

    class Solution {
    public:
        bool isValidBST(TreeNode *root) {
            return isBST(root, NULL, NULL);
        }

        bool isBST(TreeNode *root, int *plower, int *pupper) {

            if (root == NULL)return true;
            if (pupper != NULL) {
                if (root->val >= *pupper)
                    return false;
            }
            if (plower != NULL) {
                if (root->val <= *plower)
                    return false;
            }

            return isBST(root->left, plower, &root->val) && isBST(root->right, &root->val, pupper);

        }
    };

};