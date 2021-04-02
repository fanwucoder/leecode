package leetcode.editor.cn;
import leetcode.editor.cn.Utils.ListNode;
//给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。 
//
// 
//
// 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marco
//s 贡献此图。 
//
// 示例: 
//
// 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
//输出: 6 
// Related Topics 栈 数组 双指针 
// 👍 97 👎 0

public class VolumeOfHistogramLcci{
     public static void main(String[] args) {
          Solution solution = new VolumeOfHistogramLcci().new Solution();
         System.out.println(solution.trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));
     }

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int trap(int[] height) {
        if (height.length==0)
            return 0;
        int left=0,right=height.length,leftMax=height[0],rightMax=0;
        int ans=0;
        while (left<right){
            if(leftMax<rightMax){
                left++;
                if(height[left]<leftMax){
                    ans+=leftMax-height[left];
                }
                leftMax=Math.max(leftMax,height[left]);
            }else{
                right--;

                if(height[right]<rightMax){
                    ans+=rightMax-height[right];
                }
                rightMax=Math.max(height[right],rightMax );

            }
        }
        return ans;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

}