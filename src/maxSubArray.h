//
// Created by fanwu on 2020/1/4.
//

#ifndef LEECODE_MAXSUBARRAY_H
#define LEECODE_MAXSUBARRAY_H

#include "common.h"
#include <vector>
#include <climits>

//最大子数组
namespace maxSubArray {
    class Solution {
    public:
        /**
         * 暴力发，根据数组的左右上限，计算所有的子序列和，然后取最大值
         * @param nums
         * @return
         */
        int maxSubArray(vector<int> &nums) {

            int maxSum = 0;
            for (int i = 0; i < nums.size(); i++) {
                for (int j = i; j < nums.size(); j++) {
                    int sum = 0;
                    for (int k = i; k < j; k++) {
                        sum += nums[k];
                    }
                    maxSum = max(sum, maxSum);
                }
            }
            return maxSum;
        }

        /**
         * 暴力发优化，前n个的和已经计算过了，就不用计算
         * @param nums
         * @return
         */
        int maxSubArray_v1(vector<int> &nums) {

            int maxSum = INT_MIN;
            for (int i = 0; i < nums.size(); i++) {
                int sum = 0;
                for (int j = i; j < nums.size(); j++) {
                    sum += nums[j];
                    maxSum = max(sum, maxSum);
                }
            }
            return maxSum;
        }

        /**
       * 分治法
       * @param nums
       * @return
       */
        int maxSubArray_v2(vector<int> &nums) {

            int sum = nums[0];
            int maxSum = nums[0];
            for (int i = 1; i < nums.size(); i++) {
                if (nums[i] > (sum + nums[i])) {//以i结尾的最大子元素和最大值，要么是以（i-1）结尾加当前，要么是当前的，再和历史最大值求和就算出来了
                    sum = nums[i];
                } else {
                    sum = (sum + nums[i]);
                }
//                if(sum>0)sum+=nums[i];
//                else sum=nums[i];

                maxSum = max(maxSum, sum);
            }
            return maxSum;
        }


    };
}
#endif //LEECODE_MAXSUBARRAY_H
