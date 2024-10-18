#include "queue.h"
#include <stdlib.h>

Queue initQueue() {
    Queue qp = (Queue)malloc(sizeof(QType));
    qp->head = qp->tail = 0;
    return qp;
}

int empty(Queue Q) { return (Q->head == Q->tail); }

void enqueue(Queue Q, datatype n) {
    if (Q->tail == MaxQ - 1)
        Q->tail = 0;
    else
        ++(Q->tail);
    if (Q->tail == Q->head) {
        printf("\nQueue is full\n");
        exit(1);
    }
    Q->QA[Q->tail] = n;
}

datatype dequeue(Queue Q) {
    if (empty(Q)) {
        printf("\nAttempt to remove from an empty queue\n");
        exit(1);
    }
    if (Q->head == MaxQ - 1)
        Q->head = 0;
    else
        ++(Q->head);
    return Q->QA[Q->head];
}
