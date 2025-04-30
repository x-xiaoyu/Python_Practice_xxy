// Problem: 114.flatten-binary-tree-to-linked-list
// Medium 2pts
// 04/24/2024
// Topics: Linked List, Stack, Tree, DFS, Binary Tree

// Description: Given the root of a binary tree, flatten the tree into a "linked list":
//The "linked list" should use the same TreeNode class 
//where the right child pointer points to the next node in the list and the left child pointer is always null.
//The "linked list" should be in the same order as a pre-order traversal of the binary tree.

// Links:https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

void flatten(struct TreeNode* root) {
    //If the root is empty or is a leaf node, just return it.
    if (root == NULL || (root->left == NULL && root->right == NULL)) {
        return;
    }

    // If the left subtree is not empty, first unfold the left subtree
    if (root->left != NULL) {
        flatten(root->left);

        // Temporarily saving the right subtree
        struct TreeNode* tempRight = root->right;
        // Move the expanded left subtree to the right subtree position
        root->right = root->left;
        root->left = NULL; // Empty the left subtree

        // Find the rightmost node of the current right subtree
        struct TreeNode* current = root->right;
        while (current->right != NULL) {
            current = current->right;
        }

        // Attach the original right subtree to the rightmost node of the current right subtree.
        current->right = tempRight;
    }

    // Expand the original right subtree
    flatten(root->right);
}
