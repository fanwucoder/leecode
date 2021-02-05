//中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。 
//
// 例如： 
//
// 
// [2,3,4]，中位数是 3 
// [2,3]，中位数是 (2 + 3) / 2 = 2.5 
// 
//
// 给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗
//口中元素的中位数，并输出由它们组成的数组。 
//
// 
//
// 示例： 
//
// 给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。 
//
// 
//窗口位置                      中位数
//---------------               -----
//[1  3  -1] -3  5  3  6  7       1
// 1 [3  -1  -3] 5  3  6  7      -1
// 1  3 [-1  -3  5] 3  6  7      -1
// 1  3  -1 [-3  5  3] 6  7       3
// 1  3  -1  -3 [5  3  6] 7       5
// 1  3  -1  -3  5 [3  6  7]      6
// 
//
// 因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。 
//
// 
//
// 提示： 
//
// 
// 你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。 
// 与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。 
// 
// Related Topics Sliding Window 
// 👍 183 👎 0

package leetcode.editor.cn;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

//java:滑动窗口中位数
public class P480SlidingWindowMedian {
    public static void printArray(double[] arr){
        StringBuilder builder=new StringBuilder();
        for (int i=0;i<arr.length;i++){
            builder.append((int)arr[i]).append(",");
        }
        System.out.println(builder.toString());
    }
    public static void main(String[] args) {
        Solution solution = new P480SlidingWindowMedian().new Solution();
//        int i=0;
//        i++;
//        System.out.println(i);
        printArray(solution.medianSlidingWindow(new int[]{1,3,-1,-3,5,3,6,7},3));
    }

    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public double[] medianSlidingWindow(int[] nums, int k) {
            DualHeap heap = new DualHeap(k);
            double[] ans = new double[nums.length - k + 1];
            for (int i = 0; i < k; i++) {
                heap.insert(nums[i]);
            }
            ans[0] = heap.getMedian();
            for (int i = k ; i < nums.length; i++) {
                heap.insert(nums[i]);
                heap.erase(nums[i - k]);
                ans[i-k+1]=heap.getMedian();
            }
            return ans;
        }
    }

    class DualHeap {
        private PriorityQueue<Integer> small;
        private PriorityQueue<Integer> big;
        private Map<Integer, Integer> delayed;
        private Integer smallSize;
        private Integer bigSize;
        private Integer k;

        public DualHeap(int k) {
            this.k = k;
            smallSize=0;
            bigSize=0;
            small = new PriorityQueue<>(new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    return o2.compareTo(o1);
                }
            });
            big = new PriorityQueue<>(new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    return o1.compareTo(o2);
                }
            });
            delayed = new HashMap<>();
        }

        void insert(Integer num) {
            if (small.isEmpty() || num<=small.peek() ) {
                small.offer(num);
                smallSize++;
            } else {
                big.offer(num);
                bigSize++;
            }
            makeBalance();
        }
        void erase(Integer num) {
            delayed.put(num, delayed.getOrDefault(num, 0) + 1);
            if (num <= small.peek()) {
                smallSize--;
                //装箱陷阱
                if (num==small.peek()) {
                    prune(small);
                }
            } else {
                bigSize--;
                //装箱陷阱
                if (num ==big.peek()) {
                    prune(big);
                }
            }
            makeBalance();
        }

        void prune(PriorityQueue<Integer> heap) {
            while (!heap.isEmpty()) {
                int num = heap.peek();
                if (delayed.containsKey(num)) {
                    delayed.put(num, delayed.get(num) - 1);
                    //拆箱陷阱
                    if (delayed.get(num) == 0) {
                        delayed.remove(num);
                    }
                    heap.poll();
                } else {
                    break;
                }
            }
        }
        private void makeBalance() {
            if (smallSize > bigSize + 1) {
                big.offer(small.poll());
                smallSize--;
                bigSize++;
                prune(small);
            } else if (smallSize < bigSize ) {
                small.offer(big.poll());
                smallSize++;
                bigSize--;
                prune(big);
            }
        }

        public double getMedian() {
            return (k & 1) == 1 ? small.peek() : ((double) small.peek() + (double)big.peek()) / 2;

        }


    }
//leetcode submit region end(Prohibit modification and deletion)

}