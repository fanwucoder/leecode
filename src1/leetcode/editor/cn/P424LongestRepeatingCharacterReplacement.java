//给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
// 
//
// 注意：字符串长度 和 k 不会超过 104。 
//
// 
//
// 示例 1： 
//
// 
//输入：s = "ABAB", k = 2
//输出：4
//解释：用两个'A'替换为两个'B',反之亦然。
// 
//
// 示例 2： 
//
// 
//输入：s = "AABABBA", k = 1
//输出：4
//解释：
//将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
//子串 "BBBB" 有最长重复字母, 答案为 4。
// 
// Related Topics 双指针 Sliding Window 
// 👍 270 👎 0

package leetcode.editor.cn;

//java:替换后的最长重复字符
public class P424LongestRepeatingCharacterReplacement {
    public static void main(String[] args) {
        Solution solution = new P424LongestRepeatingCharacterReplacement().new Solution();
        System.out.println(solution.characterReplacement("ABAB",2));
    }

    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public int characterReplacement(String s, int k) {
            int len = s.length();
            int left = 0;
            int right = 0;
            int maxCount = 0;
            int[] charCount = new int[26];
            int res=0;
            while (right < len) {
                charCount[s.charAt(right) - 'A']++;
                maxCount = Math.max(maxCount, charCount[s.charAt(right) - 'A']);
                right++;
                if(right-left-maxCount>k){
                    charCount[s.charAt(left) - 'A']--;
                    left++;
                }
                res=Math.max(res,right-left);
            }
            return res;
        }

    }
//leetcode submit region end(Prohibit modification and deletion)

}