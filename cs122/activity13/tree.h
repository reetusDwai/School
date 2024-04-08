typedef char DataType;

typedef struct Node{
  DataType item;
  struct Node* leftChild;
  struct Node* rightChild;
}Node, *NodePtr;

typedef struct{
  NodePtr root;
 
}BinaryTree, *BinaryTreePtr;

BinaryTreePtr initBinaryTree();
NodePtr buildBT();
NodePtr newNode(DataType d);
void printBinaryTree(NodePtr np);
void printNode(NodePtr np);
int count(NodePtr root);
int height(NodePtr);
void printBinaryTree_inorder(NodePtr, int);
void printBinaryTree_postorder(NodePtr, int);
