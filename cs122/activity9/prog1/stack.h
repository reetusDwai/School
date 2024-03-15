#include<stdio.h>
#include<stdlib.h>
typedef int datatype;
#define R -999
#define StackMax 10

typedef struct{
  int top;
  datatype StackArray[StackMax];
}StackType, *StackPtr;


StackPtr initStack();
int empty(StackPtr sp);
void push(StackPtr sp, datatype input);
datatype pop(StackPtr sp);

