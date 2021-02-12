package leetcode.editor.cn;
//java:数据流中的第 K 大元素
//设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。 
//
// 请实现 KthLargest 类： 
//
// 
// KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。 
// int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。 
// 
//
// 
//
// 示例： 
//
// 
//输入：
//["KthLargest", "add", "add", "add", "add", "add"]
//[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
//输出：
//[null, 4, 5, 5, 8, 8]
//
//解释：
//KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
//kthLargest.add(3);   // return 4
//kthLargest.add(5);   // return 5
//kthLargest.add(10);  // return 5
//kthLargest.add(9);   // return 8
//kthLargest.add(4);   // return 8
// 
//
// 
//提示：
//
// 
// 1 <= k <= 104 
// 0 <= nums.length <= 104 
// -104 <= nums[i] <= 104 
// -104 <= val <= 104 
// 最多调用 add 方法 104 次 
// 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素 
// 
// Related Topics 堆 设计 
// 👍 224 👎 0

import java.util.Comparator;
import java.util.PriorityQueue;

public class P703KthLargestElementInAStream {
    public static void main(String[] args) {
        KthLargest kthLargest = new P703KthLargestElementInAStream().new KthLargest(3, new int[]{4, 5, 8, 2});
        System.out.println(kthLargest.add(3));     // return 4
        System.out.println(kthLargest.add(5)); // return 5
        System.out.println(kthLargest.add(10));  // return 5
        System.out.println(kthLargest.add(9));   // return 8
        System.out.println(kthLargest.add(4));   // return 8


    }

    //leetcode submit region begin(Prohibit modification and deletion)
    class KthLargest {
        private int k = 0;
        private int size;
        private int[] data;
        private int capcity;

        public KthLargest(int k, int[] nums) {
            this.k = k;
            size = k;
            data = new int[size];
            capcity = 0;

            for (int i = 0; i < nums.length; i++) {
                if (capcity < size - 1) {
                    data[capcity++] = nums[i];
                } else
                    this.add(nums[i]);
            }
        }

        public int add(int val) {
            if (capcity < k) {
                data[capcity++] = val;
                for (int i = capcity - 1; i >= 0; i--) shiftdown(i);
            } else {
                if (val <= data[0]) return data[0];
                data[0] = val;
                shiftdown(0);
            }
            return data[0];


        }

        private void shiftdown(int i) {
            while (i*2+1<size){
                int j=i*2+1;
                if(j<size-1&&data[j+1]<data[j]) j++;
                if(data[j]<data[i]){
                    swap(i,j);
                }else{
                    break;
                }
                i=j;
            }
        }

        public void swap(int i, int j) {
            int t = data[i];
            data[i] = data[j];
            data[j] = t;
        }
    }

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
//leetcode submit region end(Prohibit modification and deletion)

}