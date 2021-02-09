package leetcode.editor.cn;
//java:[992]K 个不同整数的子数组
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
// 👍 193 👎 0
//至多出现k个子数组-最低出现k-1个子数组
public class P992SubarraysWithKDifferentIntegers {
    public static void main(String[] args){
        Solution solution = new P992SubarraysWithKDifferentIntegers().new Solution();
        System.out.println(solution.subarraysWithKDistinct(new int[]{1,2,1,2,3},2));
        System.out.println(solution.subarraysWithKDistinct(new int[]{1,2,1,3,4},3));
    }
    //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        int num1[]=new int[A.length+1];
        int num2[]=new int[A.length+1];
        int i=0,i1=0,j=0;
        int to1=0;int to2=0;
        int ret=0;
        int n=A.length;
        while(j<n){
            if(num1[A[j]]==0){
                to1++;
            }
            num1[A[j]]++;
            if(num2[A[j]]==0){
                to2++;
            }
            num2[A[j]]++;
            while (to1>K){
                num1[A[i]]--;
                if(num1[A[i]]==0){
                    to1--;
                }
                i++;
            }
            while (to2>K-1){
                num2[A[i1]]--;
                if(num2[A[i1]]==0){
                    to2--;
                }
                i1++;
            }

            ret+=i1-i;
            j++;
        }
        return ret;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

}