#include <stdio.h>

typedef struct node{
    int number;
    char op;
    struct node* left;
    struct node* right;
} Node, *Nodeptr;

Nodeptr createNode(int, char);
Nodeptr parseStr(char*, Nodeptr);
