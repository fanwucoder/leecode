package leetcode.editor.cn;
//java:K 个不同整数的子数组
//给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。 
//
// （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。） 
//
// 返回 A 中好子数组的数目。 
//
// 
//
// 示例 1： 
//
// 输入：A = [1,2,1,2,3], K = 2
//输出：7
//解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
// 
//
// 示例 2： 
//
// 输入：A = [1,2,1,3,4], K = 3
//输出：3
//解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
// 
//
// 
//
// 提示： 
//
// 
// 1 <= A.length <= 20000 
// 1 <= A[i] <= A.length 
// 1 <= K <= A.length 
// 
// Related Topics 哈希表 双指针 Sliding Window 
// 👍 196 👎 0

import java.util.HashMap;
import java.util.Map;

public class P992SubarraysWithKDifferentIntegers_bad {
    public static void main(String[] args){
        Solution solution = new P992SubarraysWithKDifferentIntegers_bad().new Solution();
        System.out.println(solution.subarraysWithKDistinct(new int[]{1,2,1,2,3},2));
        System.out.println(solution.subarraysWithKDistinct(new int[]{1,2,1,3,4},3));
        System.out.println(solution.subarraysWithKDistinct(new int[]{1,2,3,4},4));
    }
    //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {

        int ret=0;
        int n=A.length;
        for (int k=K;k<=n;k++){
            int i=0,j=0;
//            System.out.println(k);
            Map<Integer,Integer> num=new HashMap<>();
            while (j<n){
                if(j-i<k){
                   int x= num.getOrDefault(A[j],0);
                   x+=1;
                   num.put(A[j],x);
                   j++;
                   if(num.size()==K&&j-i==k){
                        ret++;

                   }
                }else{
                    int x= num.getOrDefault(A[i],0);
                    x-=1;
                    if(x==0){
                        num.remove(A[i]);
                    }else {
                        num.put(A[i],x);
                    }
                    i++;

                }
            }
        }
        return ret;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

}