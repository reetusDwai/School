typedef  int datatype1;
typedef struct{
    char productName[20];
    float price;
    int qty;
}datatype2;

typedef struct node{
    datatype1 key;
    datatype2 value;
    struct node *left, *right;
}Node, *NodePtr;

typedef struct {
    NodePtr root;
}BST, *BSTPtr;

datatype2 search(datatype1 skey, NodePtr root);
NodePtr insert(NodePtr x,datatype1 inskey, datatype2 value);
NodePtr createNewNode(datatype1, datatype2);
BSTPtr intiBST();
void printTree(int level, NodePtr np);
int count();
