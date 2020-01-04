//
// Created by admin on 2019/12/26.
//

#include "test_data.h"

#include "gtest/gtest.h"
#include "../src/Solution.h"
#include "../src/StrStr.h"
#include "../src/LongestCommonPrefix.h"
#include <vector>
#include "../src/IsPalindromelink.h"
#include "../src/isSymmetric.h"
#include "../src/maxSubArray.h"

namespace StrStr {
    class Solution;
};

int add(int a, int b) {
    return a + b;
}


TEST(testMyAtoi, c1) {
    myAtoi::Solution solution;
    EXPECT_EQ(42, solution.myAtoi("42"));
    EXPECT_EQ(4193, solution.myAtoi("4193 with words"));
    EXPECT_EQ(0, solution.myAtoi("words and 987"));
    EXPECT_EQ(INT_MIN, solution.myAtoi("-91283472332"));
    EXPECT_EQ(INT_MAX, solution.myAtoi("91283472332"));
    EXPECT_EQ(1, solution.myAtoi("+1"));
    EXPECT_EQ(0, solution.myAtoi("+-2"));
}

TEST(testStrStr, c1) {

    cout << INT_MAX << endl;
    StrStr::Solution s;
    EXPECT_EQ(1, s.strStr("1234", "234"));
    EXPECT_EQ(0, s.strStr("1234", "123"));
    EXPECT_EQ(0, s.strStr("123", "123"));
    EXPECT_EQ(0, s.strStr("123", "12"));
    EXPECT_EQ(1, s.strStr("123", "23"));
    EXPECT_EQ(-1, s.strStr("123", "231"));

}

TEST(longestCommonPrefix, c1) {


    longestCommonPrefix::Solution s;
    string s1[] = {"flower", "flow", "flight"};
    auto a = vector<string>(s1, s1 + 3);
    EXPECT_EQ("fl", s.longestCommonPrefix(a));

    string s2[] = {"dog", "racecar", "car"};
    a = vector<string>(s2, s2 + 3);
    EXPECT_EQ("", s.longestCommonPrefix(a));

    string s3[] = {"", "racecar", "car"};
    a = vector<string>(s3, s3 + 3);
    EXPECT_EQ("", s.longestCommonPrefix(a));
    string s4[] = {"abca", "abc"};
    a = vector<string>(s4, s4 + 2);
    EXPECT_EQ("abc", s.longestCommonPrefix(a));

    a = vector<string>();
    EXPECT_EQ("", s.longestCommonPrefix(a));

}

TEST(longestCommonPrefix_v1, c1) {


    longestCommonPrefix::Solution s;
    string s1[] = {"flower", "flow", "flight"};
    auto a = vector<string>(s1, s1 + 3);
    EXPECT_EQ("fl", s.longestCommonPrefix_v1(a));

    string s2[] = {"dog", "racecar", "car"};
    a = vector<string>(s2, s2 + 3);
    EXPECT_EQ("", s.longestCommonPrefix_v1(a));

    string s3[] = {"", "racecar", "car"};
    a = vector<string>(s3, s3 + 3);
    EXPECT_EQ("", s.longestCommonPrefix_v1(a));
    string s4[] = {"abca", "abc"};
    a = vector<string>(s4, s4 + 2);
    EXPECT_EQ("abc", s.longestCommonPrefix_v1(a));

    a = vector<string>();
    EXPECT_EQ("", s.longestCommonPrefix_v1(a));

}

TEST(IsPalindromelink, c1) {


    IsPalindromelink::Solution s;
    EXPECT_EQ(true, s.isPalindrome(NULL));
    int a[3] = {1, 2, 1};
    auto l = IsPalindromelink::makeList(a, 0, 3);
    EXPECT_EQ(true, s.isPalindrome(l));
    int a1[3] = {1, 2, 2};
    l = IsPalindromelink::makeList(a1, 0, 3);
    EXPECT_EQ(false, s.isPalindrome(l));
    int a3[] = {1, 2, 2, 1};
    l = IsPalindromelink::makeList(a3, 0, 4);
    EXPECT_EQ(true, s.isPalindrome(l));
    int a4[] = {1};
    l = IsPalindromelink::makeList(a4, 0, 1);
    EXPECT_EQ(true, s.isPalindrome(l));
//    EXPECT_EQ(0, s.strStr("1234","123"));
//    EXPECT_EQ(0, s.strStr("123","123"));
//    EXPECT_EQ(0, s.strStr("123","12"));
//    EXPECT_EQ(1, s.strStr("123","23"));
//    EXPECT_EQ(-1, s.strStr("123","231"));

}

TEST(isSymmetric, c1) {
    int arr[] = {1, 2, 2, 3, 4, 4, 3};
    int len = sizeof(arr) / sizeof(arr[0]);

    int **arr1 = new int *[len];
    for (int i = 0; i < len; ++i) {
        arr1[i] = &arr[i];
    }
    isSymmetric::TreeNode *a = NULL;
    isSymmetric::TreeNode *t = creatBTree(arr1, 0, a);
    isSymmetric::Solution s;
//    PrevOrderTraversal(t);
    EXPECT_EQ(true, s.isSymmetric(t));
}

TEST(maxSubArray, c1) {

    maxSubArray::Solution s;
//    PrevOrderTraversal(t);
    int vv[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    vector<int> v = vector<int>(vv, vv +  sizeof(vv)/ sizeof(int));
    EXPECT_EQ(6, s.maxSubArray(v));
    EXPECT_EQ(6, s.maxSubArray_v1(v));
    EXPECT_EQ(6, s.maxSubArray_v2(v));
}

GTEST_API_ int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
