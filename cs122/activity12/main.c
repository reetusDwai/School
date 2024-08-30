#include<stdio.h>
#include"BST.h"
#include<string.h>

int main()
{
    int cont=1;
    datatype1 k;
    datatype2 v;
    BSTPtr mytree;
    mytree=intiBST();

    // insert product records into the BST
    while(cont){
        printf("Enter Product info, key, name, price, qty\n");
        scanf("%d%s%f%d",&k, v.productName, &v.price, &v.qty);
        mytree->root=insert(mytree->root,k, v);
        printf("Insert more product?0 or 1");
        scanf("%d",&cont);
    }

    //print Tree
    printTree(1, mytree->root);

    // search for item


    printf("Which product you want its info:");
    scanf("%d", &k);
    v=search(k, mytree->root);
    if(strcmp(v.productName, "Not Found")==0)
        printf(" No such a product!");
    else
        printf("%s, %f, %d \n", v.productName, v.price, v.qty); 

}
