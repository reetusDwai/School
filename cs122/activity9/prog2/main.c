#include"stack.h"

void print(StackPtr sp);

int main()
{
  StackPtr sp1;
  sp1=initStack();
  push(sp1, 12);
  int c=pop(sp1);
  push(sp1, 14);
  printf("%d\n", pop(sp1));
  printf("%d\n", pop(sp1));
}

void print(StackPtr sp)
{
  if(!empty(sp)){
    printf("%d ", pop(sp));
    print(sp);
  }
}
