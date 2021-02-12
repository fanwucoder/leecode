package leetcode.editor.cn;
//java:字符串的排列
//给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。 
//
// 换句话说，第一个字符串的排列之一是第二个字符串的子串。 
//
// 示例1: 
//
// 
//输入: s1 = "ab" s2 = "eidbaooo"
//输出: True
//解释: s2 包含 s1 的排列之一 ("ba").
// 
//
// 
//
// 示例2: 
//
// 
//输入: s1= "ab" s2 = "eidboaoo"
//输出: False
// 
//
// 
//
// 注意： 
//
// 
// 输入的字符串只包含小写字母 
// 两个字符串的长度都在 [1, 10,000] 之间 
// 
// Related Topics 双指针 Sliding Window 
// 👍 258 👎 0

public class P567PermutationInString {
    public static void main(String[] args) {
        Solution solution = new P567PermutationInString().new Solution();
        System.out.println(solution.checkInclusion("ab","eidbaooo"));
        System.out.println(solution.checkInclusion("ab", "eidboaoo"));
    }


    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public boolean checkInclusion(String s1, String s2) {
            int wc1[] = new int[26];
            int wc2[] = new int[26];
            int i = 0, j = 0;
            int n1 = s1.length();
            int n2 = s2.length();
            for (int k = 0; k < n1; k++) {
                wc1[s1.charAt(k) - 'a']++;
            }
            int pc1 = 0;
            int pc2 = 0;
            for (int k = 0; k < 26; k++) {
                if (wc1[k] > 0) {
                    pc1++;
                }
            }
            while (j < n2) {
                if (wc1[s2.charAt(j) - 'a'] > 0) {
                    wc2[s2.charAt(j) - 'a']++;
                    if (wc2[s2.charAt(j) - 'a'] == wc1[s2.charAt(j) - 'a']) {
                        pc2++;
                    }

                }
                j++;
                while (pc1==pc2){
                    if(j-i==n1){
                        return true;
                    }
                    if(wc1[s2.charAt(i)-'a']>0){
                        wc2[s2.charAt(i)-'a']--;
                        if(wc2[s2.charAt(i)-'a']<wc1[s2.charAt(i)-'a']){
                            pc2--;
                        }
                    }
                    i++;
                }
            }
            return false;
        }

    }
//leetcode submit region end(Prohibit modification and deletion)

}