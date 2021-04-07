package leetcode.editor.cn;
//java:杨辉三角 II
//给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。 
//
// 
//
// 在杨辉三角中，每个数是它左上方和右上方的数的和。 
//
// 示例: 
//
// 输入: 3
//输出: [1,3,3,1]
// 
//
// 进阶： 
//
// 你可以优化你的算法到 O(k) 空间复杂度吗？ 
// Related Topics 数组 
// 👍 229 👎 0

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

public class P119PascalsTriangleIi{
    public static void main(String[] args){
        Solution solution = new P119PascalsTriangleIi().new Solution();
        List<Integer> nums=solution.getRow(33);
        String a= nums.stream().map(Object::toString).collect(Collectors.joining(","));
        System.out.println(a);
//        for (Integer x:nums             ) {
//            System.out.println(x);
//        }
    }
    //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> nums=new ArrayList<>(rowIndex);
        for (int i=0;i<=rowIndex;i++){
            int j;
            int first=0;
            for(j=0;j<i;j++){
                int cur=nums.get(j);
                int x=cur+first;
                nums.set(j,x);
                first=cur;

            }
            nums.add(j,1);
            String a= nums.stream().map(Object::toString).collect(Collectors.joining(","));
            System.out.println("{"+a+"},");
        }
        return nums;
    }
}
    class Solution1 {
        public List<Integer> getRow(int rowIndex) {
            Integer[] row=new Integer[rowIndex+1];
//            List<Integer> row=new ArrayList<>(rowIndex);
            row[0]=1;
            for (int i = 1; i <= rowIndex; ++i) {
                row[i]=(int)((long) row[i - 1] * (rowIndex - i + 1) / i);
            }
            return Arrays.asList(row);
        }
    }
//leetcode submit region end(Prohibit modification and deletion)

}