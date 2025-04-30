// Problem: 24.swap-nodes-in-pairs
// Medium 2pts
// 04/24/2024
// Topics: Linked List, Recursion

// Description: Given a linked list, 
//swap every two adjacent nodes and return its head.
// You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


// Links:https://leetcode.com/problems/swap-nodes-in-pairs/description/

struct ListNode* swapPairs(struct ListNode* head) {
    // create a new node called dummy
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prev = &dummy;

    // go through entire list, and two node each time
    while (prev->next != NULL && prev->next->next != NULL) {
        struct ListNode *first = prev->next;         // first node
        struct ListNode *second = prev->next->next;  // second node

        // switch
        first->next = second->next;
        second->next = first;
        prev->next = second;

        // move the pointer of prev to the previous of the one that needed to be switched
        prev = first;
    }

    // return new head node, which is the next node of dummy.
    return dummy.next;
}