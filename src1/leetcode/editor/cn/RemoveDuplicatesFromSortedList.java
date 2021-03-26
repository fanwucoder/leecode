package leetcode.editor.cn;

//存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。 
//
// 返回同样按升序排列的结果链表。 
//
// 
//
// 示例 1： 
//
// 
//输入：head = [1,1,2]
//输出：[1,2]
// 
//
// 示例 2： 
//
// 
//输入：head = [1,1,2,3,3]
//输出：[1,2,3]
// 
//
// 
//
// 提示： 
//
// 
// 链表中节点数目在范围 [0, 300] 内 
// -100 <= Node.val <= 100 
// 题目数据保证链表已经按升序排列 
// 
// Related Topics 链表 
// 👍 511 👎 0

import leetcode.editor.cn.Utils.ListNode;

public class RemoveDuplicatesFromSortedList{

     // Definition for singly-linked list.

     public static void main(String[] args) {
          Solution solution = new RemoveDuplicatesFromSortedList().new Solution();
        Utils.printList(solution.deleteDuplicates(Utils.getListNode(new int[]{1,1,2,3,4,5,6,6})));
         Utils.printList(solution.deleteDuplicates(Utils.getListNode(new int[]{})));
     }

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates1(ListNode head) {
        if(head==null||head.next==null){
            return head;
        }
        ListNode next = head.next;
        if(head.val==next.val){
            head=deleteDuplicates1(next.next);
        }else {
            head.next=deleteDuplicates1(next);
        }
        return head;
    }
    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur=head;
        ListNode next;
        while (cur!=null&&cur.next!=null){
            next=cur.next;
            if(cur.val==next.val){
                cur.next=next.next;
            }else {
                cur=cur.next;
            }
        }
        return head;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

}