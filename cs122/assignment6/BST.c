#include<stdio.h>
#include<stdlib.h>
#include"BST.h"
#include<string.h>
datatype2 search(datatype1 skey, NodePtr root)
{
	NodePtr curr=root;
	while(curr!=NULL)
	{
		if(skey<curr->key) curr=curr->left;
		else if (skey>curr->key) curr=curr->right;
		else if(skey==curr->key) return curr->value;
		
	}
	datatype2 notfound;
	strcpy(notfound.productName,"Not Found");
	notfound.price=-1;
	notfound.qty=0;
	
	return notfound;
}

NodePtr insert(NodePtr x,datatype1 inskey, datatype2 value)
{
	if(x==NULL) return createNewNode(inskey,value);
	if(inskey<x->key) x->left=insert(x->left, inskey, value);
	else if(inskey>x->key) x->right=insert(x->right,inskey, value);
	else if(inskey=x->key) x->value=value;
	return x;
}	



NodePtr createNewNode(datatype1 insKey, datatype2 value){
  NodePtr np=(NodePtr)malloc(sizeof(Node));
  np->key=insKey;
  np->value=value;
  np->left=NULL;
  np->right=NULL;
  return np;
  
}

BSTPtr intiBST()
{
  BSTPtr BSTp=(BSTPtr)malloc(sizeof(BST));
  BSTp->root=NULL;
  return BSTp;
}

void printTree(int level, NodePtr np){
  if(np){
    printf("%*c%d %s %f %d\n",level,' ', np->key, np->value.productName,np->value.price, np->value.qty);
    printTree(++level, np->left);
    printTree(++level, np->right);
	   }
  }
