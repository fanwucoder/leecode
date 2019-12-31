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
        string longestCommonPrefix_v1(vector<string> &strs) {
            if(strs.empty())
                return "";
            string sub = "";
            auto end=strs[0].size();
            for (int i = 1; i < strs.size(); ++i) {
                auto new_end=0;
                for (int j=0;j<end&&j<strs[0].size();j++) {
                    if(strs[0][j]==strs[i][j]){
                        new_end++;
                    } else{
                        break;
                    }
                }
                end=new_end;

//                cout<<endl;
//                cout<<sub<<endl;
            }
            return strs[0].substr(0,end);

        }
    };
}
#endif //LEECODE_LONGESTCOMMONPREFIX_H
