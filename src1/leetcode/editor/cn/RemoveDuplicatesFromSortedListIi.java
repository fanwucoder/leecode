package leetcode.editor.cn;

//给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。 
//
// 示例 1: 
//
// 输入: 1->2->3->3->4->4->5
//输出: 1->2->5
// 
//
// 示例 2: 
//
// 输入: 1->1->1->2->3
//输出: 2->3 
// Related Topics 链表 
// 👍 512 👎 0

public class RemoveDuplicatesFromSortedListIi{
    //Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
     public static void main(String[] args) {
          Solution solution = new RemoveDuplicatesFromSortedListIi().new Solution();
     
     }

//leetcode submit region begin(Prohibit modification and deletion)


class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dump=new ListNode();
        dump.next=head;
        ListNode pre=dump;
        ListNode cur=head;
        ListNode next;
        while (cur!=null&&cur.next!=null){
            next=cur.next;
            if(cur.val!=next.val){
                pre=cur;
            }else {
                while (next!=null&&cur.val==next.val){
                    next=next.next;
                }
                pre.next=next;
            }
            cur=next;
        }
        return  dump.next;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

}