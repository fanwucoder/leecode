//
// Created by admin on 2019/12/31.
//

#ifndef LEECODE_ISPALINDROMELINK_H
#define LEECODE_ISPALINDROMELINK_H
#include <iostream>
using namespace std;

//Definition for singly-linked list.
namespace IsPalindromelink {
    struct ListNode {
        int val;
        ListNode *next;

        ListNode(int x) : val(x), next(NULL) {}
    };
    ListNode* makeList(int a[],int pos,int len){
        ListNode* head=new ListNode(a[0]);
        auto cur=head;
        for (int i = 1; i < len; ++i) {
            auto node=new ListNode(a[i]);
            cur->next=node;
            cur=cur->next;
        }
        return head;
    }
    void printList(ListNode* head){
        while (head!= nullptr){
            cout<<head->val<<',';
            head=head->next;
        }
        cout<<endl;
    }
    class Solution {
    public:
        bool isPalindrome(ListNode *head) {
            auto slow = head;
            auto quick = head;
            ListNode *rhead = nullptr;
            if(head== nullptr||head->next== nullptr){
                return true;
            }
            while (quick != NULL) {
                if (quick->next)
                    quick = quick->next->next;
                else {
                    break;
                }
                auto temp = slow->next;
                slow->next = rhead;
                rhead = slow;
                slow = temp;

            }
            if (quick == nullptr) {
                quick = slow;
                slow=rhead;
            } else{
                quick=slow->next;
                slow=rhead;
            }
//            printList(quick);
//            printList(slow);
            while (slow!=nullptr && quick!= nullptr){
                if(slow->val!=quick->val){
                    return false;
                }
                slow=slow->next;
                quick=quick->next;
            }
            return true;
        }
    };

}
#endif //LEECODE_ISPALINDROMELINK_H
