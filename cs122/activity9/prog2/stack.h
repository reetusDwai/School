#include<stdio.h>
#include<stdlib.h>
typedef int datatype;
#define R -999
typedef struct node{
   datatype data;
  struct node *next;
}Node, *NodePtr;

typedef struct{
  NodePtr top;
}StackType, *StackPtr;


StackPtr initStack();
int empty(StackPtr sp);
void push(StackPtr sp, datatype input);
datatype pop(StackPtr sp);

