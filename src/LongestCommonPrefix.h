//
// Created by fanwu on 2019/12/28.
//

#ifndef LEECODE_LONGESTCOMMONPREFIX_H
#define LEECODE_LONGESTCOMMONPREFIX_H

#include <algorithm>
#include <string>
#include <vector>
#include <list>

using namespace std;
namespace longestCommonPrefix {
    class Solution {
    public:
        string longestCommonPrefix(vector<string> &strs) {
            auto lens = vector<int>();
            for (auto s : strs) {
                lens.push_back(s.size());
            }
            auto len = min_element(begin(lens), end(lens));
            if(len .base()==NULL)
                return "";
            string sub = "";
            for (int i = 0; i < *len; ++i) {
                auto a = strs[0][i];
                for (auto s:strs) {

                    if (s[i] != a)
                        return sub;

                }
                sub += a;
//                cout<<endl;
//                cout<<sub<<endl;
            }
            return sub;
        }
    };
}
#endif //LEECODE_LONGESTCOMMONPREFIX_H
