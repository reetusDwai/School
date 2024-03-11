#include <stdio.h>
#include <stdlib.h>
#define MaxQ 12

typedef struct {
  int a;
} datatype;

typedef struct {
  int head, tail;
  datatype QA[MaxQ];
} QType, *Queue;

Queue initQueue();
int empty(Queue Q);
void enqueue(Queue Q, datatype n);
datatype dequeue(Queue Q);
