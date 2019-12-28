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
            if (strs.size() == 0)
                return "";
            string sub = "";
            for (int i = 0; i < strs[0].size(); ++i) {
                auto a = strs[0][i];
                auto flag=true;
                for (auto s:strs) {
                    if (i < s.size()) {
                        if (s[i] != a)
                            return sub;
                    }else{
                        flag=false;
                        break;
                    }
                }
                if(!flag)
                    break;
                sub += a;
//                cout<<endl;
//                cout<<sub<<endl;
            }
            return sub;
        }
    };
}
#endif //LEECODE_LONGESTCOMMONPREFIX_H
