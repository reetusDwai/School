#include "stack.h"

StackPtr initStack() {
    StackPtr sp = (StackPtr) malloc(sizeof(StackType));
    sp -> top = -1;
    return sp;
}
int empty(StackPtr sp) {
    return (sp -> top ==-1);
}
void push(StackPtr sp,datatype input) {
    (sp->top)++;
    if(sp->top<StackMax)
        sp->StackArray[sp->top]=input;
    else
        printf("stack overflow!\n");
}
datatype pop(StackPtr sp) {
    if (empty(sp)) return R;
    datatype output = sp -> StackArray[sp->top];
    --(sp->top);
    return output;
}

