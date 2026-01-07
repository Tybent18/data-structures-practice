#include <stdio.h>
#include <stdlib.h>
#include "bintree.h"

/* Create a new tree node */
BTNode *create(int value) {
    BTNode *node = malloc(sizeof *node);
    if (node == NULL) {
        perror("malloc failed");
        return NULL;
    }

    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

/* Insert a node into the BST */
BTNode *insert(BTNode *root, BTNode *node) {
    if (root == NULL) {
        return node;
    }

    if (node->value <= root->value) {
        root->left = insert(root->left, node);
    } else {
        root->right = insert(root->right, node);
    }

    return root;
}

/* Delete (free) the entire tree */
BTNode *deleteTree(BTNode *root) {
    if (root == NULL) {
        return NULL;
    }

    deleteTree(root->left);
    deleteTree(root->right);
    free(root);

    return NULL;
}

/* Inorder traversal */
void printInorder(const BTNode *root) {
    if (root == NULL) {
        return;
    }

    printInorder(root->left);
    printf("%d\t", root->value);
    printInorder(root->right);
}

/* Preorder traversal */
void printPreorder(const BTNode *root) {
    if (root == NULL) {
        return;
    }

    printf("%d\t", root->value);
    printPreorder(root->left);
    printPreorder(root->right);
}

/* Postorder traversal */
void printPostorder(const BTNode *root) {
    if (root == NULL) {
        return;
    }

    printPostorder(root->left);
    printPostorder(root->right);
    printf("%d\t", root->value);
}