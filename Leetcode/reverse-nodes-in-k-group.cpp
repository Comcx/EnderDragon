/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
  ListNode* reverseKGroup(ListNode* head, int k) {
    if(!head) return head;
    
    ListNode *cur(head), *a(nullptr), *suc(nullptr);
    int i(k);
    for(ListNode *p(head); p && i > 0; --i, p = p->next);
    if(i > 0) return head;
    
    for(i = k; cur && i > 0; --i, cur = suc) {
      suc = cur->next;
      cur->next = a;
      a = cur;
    }
    ListNode *rest = reverseKGroup(suc, k);
    head->next = rest;
    
    return a;
  }
};



