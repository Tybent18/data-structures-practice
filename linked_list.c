#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STR_SIZE 100

typedef struct Node {
    int value;
    char str[STR_SIZE];
    struct Node *next;
} Node;

/* Create a new node */
Node *createNode(int value, const char *str) {
    Node *node = malloc(sizeof *node);
    if (node == NULL) {
        perror("malloc failed");
        return NULL;
    }

    node->value = value;
    strncpy(node->str, str, STR_SIZE - 1);
    node->str[STR_SIZE - 1] = '\0';
    node->next = NULL;

    return node;
}

/* Add node to the front of the list */
Node *addNode(Node *head, Node *node) {
    if (node == NULL) {
        return head;
    }

    node->next = head;
    return node;
}

/* Delete the head node */
Node *deleteNode(Node *head) {
    if (head == NULL) {
        return NULL;
    }

    Node *next = head->next;
    free(head);
    return next;
}

/* Print all nodes */
void printNodes(const Node *head) {
    const Node *ptr = head;
    while (ptr != NULL) {
        printf("%d %s\n", ptr->value, ptr->str);
        ptr = ptr->next;
    }
}

/* Print a single node */
void printNode(const Node *node) {
    if (node == NULL) {
        return;
    }
    printf("Value: %d\nStr: %s\n", node->value, node->str);
}

/* Free entire list */
void freeList(Node *head) {
    while (head != NULL) {
        Node *next = head->next;
        free(head);
        head = next;
    }
}

int main(int argc, char *argv[]) {
    Node *head = NULL;

    head = addNode(head, createNode(15, "alpha"));
    head = addNode(head, createNode(20, "beta"));
    head = addNode(head, createNode(25, "gamma"));

    head = deleteNode(head);

    head = addNode(head, createNode(30, "delta"));

    printNodes(head);

    freeList(head);
    return 0;
}