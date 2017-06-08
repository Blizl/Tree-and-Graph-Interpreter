#include <iostream>
class bstNode{
    public:
        int data;
        bstNode* left;
        bstNode* right;
};

bstNode* rootPtr;

bstNode* GetNewNode(int data){
    bstNode* newNode = new bstNode();
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
bstNode* insert(bstNode* root, int data){
    if (root == NULL){
        return GetNewNode(data);
    }
    else if (data <= root->data){
        root->left = insert(root->left, data);
    }
    else{
        root->right = insert(root->right, data);
    }
    return root;
}
bool search(bstNode* root, int data){
   if(root == NULL) return false;
   else if(root->data == data) return true;
   else if(data <= root->data) return search(root->left, data);
   else return search(root->right, data);
}
int main(){
    bstNode* root = NULL;
    root = insert(root, 10);
    root = insert(root, 11);
    root = insert(root, 7);
    root = insert(root, 6);
    root = insert(root, 8); 
    int searchNum = 7;
    if (search(root, searchNum) == true)
        std::cout << "Found!";
    else
        std::cout <<  "Not found";
}