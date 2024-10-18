#include "stack.h"

StackPtr initStack() {
    StackPtr sp = (StackPtr) malloc(sizeof(StackType));
    sp -> top = NULL;
    return sp;
}
int empty(StackPtr sp) {
    return (sp -> top == NULL);
}
void push(StackPtr sp,datatype input) {
    NodePtr np = (NodePtr) malloc(sizeof(Node));
    np -> data = input;
    np -> next = sp -> top;
    sp -> top = np;
}
datatype pop(StackPtr sp) {
    if (empty(sp)) return R;
    datatype output = sp -> top -> data;
    NodePtr temp = sp -> top;
    sp -> top = sp -> top -> next;
    free(temp);
    return output;
}

