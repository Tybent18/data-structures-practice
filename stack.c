#include <stdio.h>
#include <stdlib.h>

typedef struct StackItem {
    int value;
    struct StackItem *next;
} StackItem;

/* Push a value onto the stack */
StackItem *push(StackItem *top, int value) {
    StackItem *item = malloc(sizeof *item);
    if (item == NULL) {
        perror("malloc failed");
        return top;
    }

    item->value = value;
    item->next = top;
    return item;
}

/* Pop a value from the stack */
StackItem *pop(StackItem *top, int *popResult) {
    if (top == NULL) {
        return NULL;
    }

    *popResult = top->value;
    StackItem *next = top->next;
    free(top);
    return next;
}

/* Print the stack */
void printStack(const StackItem *top) {
    const StackItem *ptr = top;
    while (ptr != NULL) {
        printf("%d\n", ptr->value);
        ptr = ptr->next;
    }
}

/* Free entire stack */
void freeStack(StackItem *top) {
    while (top != NULL) {
        StackItem *next = top->next;
        free(top);
        top = next;
    }
}

int main(int argc, char *argv[]) {
    StackItem *top = NULL;
    int popResult;

    top = push(top, 10);
    top = push(top, 20);
    top = push(top, 30);
    top = push(top, 40);

    top = pop(top, &popResult);
    top = push(top, 50);
    top = pop(top, &popResult);
    top = push(top, 60);

    printStack(top);

    freeStack(top);
    return 0;
}