		
		#include <stdlib.h>
 
        typedef struct {
           int head, tail;
           datatype QA[MaxQ];
        } QType, *Queue;
 
        Queue initQueue();
		int empty(Queue Q);
        void enqueue(Queue Q, datatype n);
        datatype dequeue(Queue Q);
		
		