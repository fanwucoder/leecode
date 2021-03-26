package leetcode.editor.cn;

import java.util.ArrayList;
import java.util.List;

public class Utils {
    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    public static ListNode getListNode(int list[]){
        ListNode dump=new ListNode();
        ListNode head=dump;
        for (int x :list) {
            head.next=new ListNode(x);
            head=head.next;
        }
        return dump.next;
    }
    public static void printList(ListNode head){
        List<String> arr=new ArrayList<>();
        while (head!=null){
            arr.add(String.valueOf(head.val));
            head=head.next;
        }

        System.out.println("["+String.join(",",arr)+"]");
    }

    public static void main(String[] args) {
        printList(getListNode(new int[]{1,1,2,3,4,4,5}));
    }
}
