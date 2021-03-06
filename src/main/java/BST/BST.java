package BST;

import AVL.AVLNode;
import BTree.BTreeNode;
import SPLAY.SPLAYNode;

/**
 * Class BST
 * Declare node root and contains all the methods to build the tree
 * @author Diego
 * @version 1.0
 * @since 21/11/2020
 */
public class BST {
    public NodeBST root;
    /**
     * BST constructor
     * @author Diego
     * @version 1.0
     * @since 21/11/2020
     */
    public BST (){
        this.root = null;
    }
    /**
     * Method insert
     * Call Recursive method
     * @param key
     * @return root;
     * @author Diego
     * @version 1.0
     * @since 21/11/2020
     */
    public void insert(int key){
        root=insertRecursive(root,key);
    }
    NodeBST insertRecursive(NodeBST root, int key){
        //tree is empty
        if (root==null){
            root=new NodeBST(key);
            return root;
        }
        //Traverse Tree
        if (key<root.key)     //insert in the left subtree
            root.left=insertRecursive(root.left, key);
        else if (key>root.key)    //insert in the right subtree
            root.right=insertRecursive(root.right, key);
        // return pointer
        return root;
    }
    /**
     * Method inorderBST
     * Call Recursive method inorder for show the Facts
     * @author Diego
     * @version 1.0
     * @since 21/11/2020
     */
    void inorderBST() {
        inorderRecursive(root);
    }
    void inorderRecursive(NodeBST root){
        if (root!=null){
            inorderRecursive(root.left);
            System.out.print(root.key+ " ");
            inorderRecursive(root.right);
        }
    }
    /**
     * Method searchBST
     * Call Recursive method for Search fact
     * @param key (search)
     * @return boolean;
     * @author Diego
     * @version 1.0
     * @since 21/11/2020
     */
    boolean searchBST(int key){
        root=searchRecursive(root,key);
        if (root!=null)
            return true;
        else
            return false;
    }
    NodeBST searchRecursive(NodeBST root, int key){
        if (root==null||root.key==key)
            return root;
        if (root.key>key)
            return searchRecursive(root.left,key);
        return searchRecursive(root.right,key);
    }
    public AVLNode insertAVL(int key){
        return new AVLNode(key);

    }

    public NodeBST insertSplay( int item) {
        return new NodeBST(item);
    }

    public void insertB(int item) {
    }
    public int maxDepth(NodeBST node){
        if (node == null){
            return 0;}
        else
        {
            int lDepth = maxDepth(node.left);
            int rDepth = maxDepth(node.right);

            if (lDepth > rDepth)
                return (lDepth + 1);
            else
                return (rDepth + 1);
        }

    }
/**
 * Main Class
 * Contain the instance for run Tree
 * @author Diego
 * @version 1.0
 * @since 21/11/2020
 */
static class Main{
    public static void main (String [] args){
        BST firtsBST=new BST();
        firtsBST.insert(45);
        firtsBST.insert(10);
        firtsBST.insert(7);
        firtsBST.insert(12);
        firtsBST.insert(90);
        firtsBST.insert(50);
        firtsBST.inorderBST();
        boolean returnTF= firtsBST.searchBST(50);
        System.out.println(returnTF);
        System.out.println("END");
    }
}
}