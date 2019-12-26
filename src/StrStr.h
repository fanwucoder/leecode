//
// Created by admin on 2019/12/26.
//

#ifndef LEECODE_STRSTR_H
#define LEECODE_STRSTR_H

#include <string>
using namespace std;

#include <iostream>


namespace StrStr {
    class Solution{
    public:
        int strStr(string haystack, string needle) {
//            cout<<haystack<<endl<<needle<<endl;
            auto  len1=haystack.size();
            auto  len2=needle.size();
            if(len1<len2)return -1;
            if(len1==len2&&len1==0) return 0;
            for (int i = 0; i <len1-len2+1; i++) {
                int j=i;
                for (; j-i < len2; j++) {
//                    cout<<haystack[j]<<needle[j-i]<<i<<j<<endl;
                    if(haystack[j]!=needle[j-i]){
                        break;
                    }
                }
                if((j-i)==len2) return i;


            }
            return -1;
        }
    };
}
#endif //LEECODE_STRSTR_H
