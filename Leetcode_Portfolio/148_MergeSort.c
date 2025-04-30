// Problem: 148.Merge Sort
// Medium 2pts
// Canvas Provided
// 04/23/2024
// Topics: Linked List, Two Pointers

// Description: Given the head of a linked list, 
//return the list after sorting it in ascending order.

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

//declare
struct ListNode* sortList(struct ListNode* head);
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2);
struct ListNode* findMiddle(struct ListNode* head);

struct ListNode* sortList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }

    struct ListNode* middle = findMiddle(head);
    struct ListNode* secondHalf = middle->next;
    middle->next = NULL; 

    struct ListNode* left = sortList(head);       // sorting for the first half of list
    struct ListNode* right = sortList(secondHalf); //sorting for the second half of list

    return mergeTwoLists(left, right);            // merge two lists that had been ordered 
}

struct ListNode* findMiddle(struct ListNode* head) {
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    struct ListNode* prev = NULL;

    while (fast != NULL && fast->next != NULL) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    return prev; // return the middle of the Node
}

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = NULL;
    struct ListNode* current = dummy;

    while (l1 != NULL && l2 != NULL) {
        if (l1->val < l2->val) {
            current->next = l1;
            l1 = l1->next;
        } else {
            current->next = l2;
            l2 = l2->next;
        }
        current = current->next;
    }

    if (l1 != NULL) {
        current->next = l1;
    } else {
        current->next = l2;
    }

    struct ListNode* head = dummy->next;
    free(dummy);
    return head;
}

