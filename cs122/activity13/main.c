#include<stdio.h>
#include"tree.h"

int main(){
    BinaryTreePtr tp=initBinaryTree();
    tp->root=buildBT();
    printBinaryTree(tp->root);
    printf("height=%d \n",height(tp->root));
    printf("inoder:\n");
    printBinaryTree_inorder(tp->root,0);
    printf("\npostorder:\n");
    printBinaryTree_postorder(tp->root,0);
    printf("\n");
}
