#include"tree.h"
#include<stdio.h>
#include<stdlib.h>
char input[25]="*+a**bc+def";
BinaryTreePtr initBinaryTree(){
    BinaryTreePtr tp=(BinaryTreePtr)malloc(sizeof(BinaryTree));
    tp->root=NULL;
}
NodePtr buildBT(){
    static int i=0;
    if(input[i]!='\0')
    {
        char t=input[i++];
        NodePtr np=newNode(t);
        if(t=='+' ||t=='*')
        {
            np->leftChild=buildBT();
            np->rightChild=buildBT();
        }
        return np;

    }
}
NodePtr newNode(DataType d){
    NodePtr np=(NodePtr)malloc(sizeof(Node));
    np->item=d;
    np->leftChild=NULL;
    np->rightChild=NULL;
    return np;
}
void printBinaryTree(NodePtr np){

    if(np==NULL)return;
    printNode(np);
    printBinaryTree(np->leftChild);
    printBinaryTree(np->rightChild);

}
void printBinaryTree_inorder(NodePtr np,int  level){

    if(np==NULL)return;

    printBinaryTree_inorder(np->leftChild, level+1);
    // for(int i=0; i<level;i++)printf(" ");
    printNode(np);
    //printf("\n");
    printBinaryTree_inorder(np->rightChild,level+1);

} 
void printBinaryTree_postorder(NodePtr np,int level){
    if(np==NULL)return;
    printBinaryTree_postorder(np->leftChild, level+1);
    printBinaryTree_postorder(np->rightChild,level+1);
    printNode(np);
} 
void printNode(NodePtr np)
{
    printf("%c ", np->item);
}
int height(NodePtr np)
{
    int x1, x2;
    if(np==NULL) return -1;
    else{
        x1=height(np->leftChild)+1;
        x2=height(np->rightChild)+1;
        return (x1>=x2?x1:x2);
    }
}
