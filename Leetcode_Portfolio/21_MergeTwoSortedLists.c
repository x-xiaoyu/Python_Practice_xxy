// Problem: 21.merge-two-sorted-lists
// Easy 1pts
// 04/23/2024
// Topics: Linked List, Recursion

// Description: You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
// Return the head of the merged linked list.


// Links: hhttps://leetcode.com/problems/merge-two-sorted-lists/description/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *head = NULL;  // pointer to the head of the result of the list
    struct ListNode **tail = &head;  // pointer's pointer, pointer to the last node of next pointer

    while (list1 != NULL && list2 != NULL) {
        if (list1->val < list2->val) {
            *tail = list1;  // connect recent node of list1 to the list of the result 
            list1 = list1->next;  // move list1
        } else {
            *tail = list2;  // connect recent node of list2 to the list of the result 
            list2 = list2->next;  // move list2
        }
        tail = &((*tail)->next);  // move the orignal tail to the new tail
    }

    // Connect with other that left
    if (list1 != NULL) {
        *tail = list1;  // if list1 has remaining, connect them
    } else if (list2 != NULL) {
        *tail = list2;  // if list2 has remaining, connect them
    }

    return head;  // return the head of the list
}