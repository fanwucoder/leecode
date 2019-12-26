//
// Created by admin on 2019/12/26.
//

#include "addTest.h"

#include "gtest/gtest.h"
#include "../src/Solution.h"
#include "../src/StrStr.h"
namespace StrStr {
      class Solution;
};
int add(int a, int b){
    return a+b;
}


TEST(testMyAtoi, c1){
    myAtoi::Solution solution;
    EXPECT_EQ(42, solution.myAtoi("42"));
    EXPECT_EQ(4193, solution.myAtoi("4193 with words"));
    EXPECT_EQ(0, solution.myAtoi("words and 987"));
    EXPECT_EQ(INT_MIN, solution.myAtoi("-91283472332"));
    EXPECT_EQ(INT_MAX, solution.myAtoi("91283472332"));
    EXPECT_EQ(1, solution.myAtoi("+1"));
    EXPECT_EQ(0, solution.myAtoi("+-2"));
}
TEST(testStrStr, c1){


    StrStr::Solution s;
    EXPECT_EQ(1, s.strStr("1234","234"));
    EXPECT_EQ(0, s.strStr("1234","123"));
    EXPECT_EQ(0, s.strStr("123","123"));
    EXPECT_EQ(0, s.strStr("123","12"));
    EXPECT_EQ(1, s.strStr("123","23"));
    EXPECT_EQ(-1, s.strStr("123","231"));

}
GTEST_API_ int main(int argc, char** argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
