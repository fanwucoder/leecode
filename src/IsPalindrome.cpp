//
// Created by admin on 2019/12/24.
//

#include "IsPalindrome.h"
#include <iostream>
#include <string>

using namespace std;
/**
 *双指针发，从两端出发，分别变遍历排除非法字符，如果字符串不相等，则返回false，否则返回true；
 */
class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = 0;
        j = static_cast<int>(s.size() - 1);
        while (i < j) {
            if (!isNumOrChar(s.at(i))) {
                i++;
                continue;
            }
            if (!isNumOrChar(s.at(j))) {
                j--;
                continue;
            }
            if (toLower(s.at(i)) != toLower(s.at(j))) {
//                cout<<toLower(s.at(i))<<toLower(s.at(j))<<endl;
//                cout<<"error"<<endl;
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    bool isNumOrChar(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9');

    }

    char toLower(char c) {
        if (c >= 'a' && c <= 'z') {
            return c;
        }
        if (c >= 'A' && c <= 'Z') {
            return static_cast<char>(c + 32);
        }
        return c;
    }
};

int main() {
    Solution s;
    cout << s.isPalindrome("A man, a plan, a canal: Panama") << endl;
    return 0;
}