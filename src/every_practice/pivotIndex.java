import java.util.Arrays;

public class pivotIndex {
    class Solution {
        public int pivotIndex(int[] nums) {
            int leftSum=0;
            int total = Arrays.stream(nums).sum();
            for (int i = 0; i < nums.length; i++) {

                if (total - nums[i] - leftSum == leftSum) {
                    return i;
                }
                leftSum+=nums[i];

            }
            return -1;

        }
    }

    private int get_center(int[] nums, boolean direct) {
        /**
         * 逻辑太复杂，放弃
         */
        int i = 0;
        int j = nums.length - 1;
        int leftSum = 0, rightSum = 0;
        if (nums.length == 0) {
            return -1;
        }
        System.out.println("-----------");
        while (i < j) {
            if (nums[j] == 0) {
                j--;
                continue;
            }
            if (nums[i] == 0) {
                nums[i]++;
                continue;
            }
            System.out.println(i);
            System.out.println(j);
            if (rightSum > leftSum) {
                if (direct) {
                    leftSum += nums[i];
                    i++;
                } else {
                    rightSum += nums[j];
                    j--;
                }

            } else if (leftSum > rightSum) {
                if (direct) {
                    rightSum += nums[j];
                    j--;
                } else {
                    leftSum += nums[i];
                    i++;
                }

            } else {
                rightSum += nums[j];
                j--;
            }
//                System.out.println(String.format("%d,%d,%d,%d",leftSum,rightSum,i,j ));

        }
        System.out.println("-------------");
        if (leftSum != rightSum) {
            return -1;
        }

        return i;

    }




    public static void main(String[] args) {
        pivotIndex p = new pivotIndex();
        Solution s = p.new Solution();
        System.out.println(s.pivotIndex(new int[]{-1, -1, 0, -1, -1, -1}));
        System.out.println(s.pivotIndex(new int[]{1, 7, 3, 6, 5, 6}));
        System.out.println(s.pivotIndex(new int[]{1, 2, 3}));

    }
}
