//
// Created by fanwu on 2020/1/1.
//

#ifndef LEECODE_ISSYMMETRIC_H
#define LEECODE_ISSYMMETRIC_H

#include <iostream>
#include <stack>
#include "common.h"

using namespace std;
namespace isSymmetric {

    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;

        TreeNode(int x = 0) : val(x), left(NULL), right(NULL) {}
    };

    class Solution {
    public:
        bool isSymmetric(TreeNode *root) {

            if (root == NULL)return true;
            if (root->left == root->right && root->left == NULL)return true;
            if (root->left != NULL && root->right != NULL) {
                auto pl = root->left;
                auto pr = root->right;
                auto s = stack<TreeNode *>();
                auto s1 = stack<TreeNode *>();
                cout << endl;
                while (pl != NULL || pr != NULL || !s.empty() || !s1.empty()) {
                    if (pl != NULL && pr != NULL) {
                        if (pl->val != pr->val)return false;
//                        cout << pl->val;
                        cout << pl->val << ',' << pr->val << endl;
                        s.push(pl);
                        s1.push(pr);
                        pl = pl->left;
                        pr = pr->right;
                    } else if (pl == NULL && pr == NULL) {
                        pl = s.top();
                        pr = s1.top();
                        s.pop();
                        s1.pop();
                        pl = pl->right;
                        pr = pr->left;
                    } else {
                        return false;
                    }
                }
                return true;
            }
            return false;
        }
    };
}
#endif //LEECODE_ISSYMMETRIC_H
