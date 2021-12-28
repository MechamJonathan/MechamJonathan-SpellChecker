public class BinarySearchTree<E extends Comparable<E>> {

    private Node root = null;

    public class Node{
        public E value;
        public Node left;
        public Node right;

        public Node(E value) {
            this.value  = value;}
    }

    boolean insert(E value) {
        if (root == null) {
            Node node = new Node(value);
            this.root = node;
            return true;
        }
        else {
            Node parent = null;
            Node node = root;
            while (node != null) {
                parent = node;
                if (value.compareTo(node.value) < 0) {
                    node = node.left;
                }
                else {
                    node = node.right;
                }
            }

            Node newNode = new Node(value);
            if (value.compareTo(parent.value) < 0){
                parent.left = newNode;
            }
            else {
                parent.right = newNode;
            }
        }
        return false;
    }



    boolean remove(E value) {
        Node parent = null;
        Node node = root;
        boolean done = false;
        while (!done) {
            if(node == null){
                return false;
            }
            if (node.value.compareTo(value) > 0) {
                parent = node;
                node = node.left;
            }
            else if (node.value.compareTo(value) < 0) {
                parent = node;
                node = node.right;
            }
            else {
                done = true;
            }
        }

        if (node.left == null) {
            if (parent == null) {
                root = node.right;
            }
            else {
                if (parent.value.compareTo(value) < 0 ) {
                    parent.right = node.right;
                }
                else {
                    parent.left = node.right;
                }
            }
        }
        else {
            Node parentOfRight = node;
            Node rightMost = node.left;
            while (rightMost.right != null) {
                parentOfRight = rightMost;
                rightMost = rightMost.right;
            }
            node.value = rightMost.value;
            if (parentOfRight.right == rightMost) {
                parentOfRight.right = rightMost.left;
            }
            else {
                parentOfRight.left = rightMost.left;
            }
        }
        return done;
    }

    boolean search(E value) {
        Node node = root;
        while (node != null && value != node.value) {
            if (value.compareTo(node.value) < 0) {
                node = node.left;
            }
            else {
                node = node.right;
            }
        }
        if (node == null) return false;
        return true;
    }

    void display(String message) {
        System.out.println(message);
        display(this.root);
        System.out.println();

    }

    private void display(Node node) {
        if (node == null) return;

        display(node.left);
        System.out.printf("%s, ", node.value);
        display(node.right);
    }

    int numberNodes() {
        return numberNodes(root);
    }

    private int numberNodes(Node node) {
        if (node == null)
            return 0;

        int totalNodes;

        //totalNodes++;

        totalNodes = (numberNodes(node.left) + numberNodes(node.right)) + 1;
        return totalNodes;
    }


    int numberLeafNodes() {
        return numberLeafNodes(root);
    }

    private int numberLeafNodes(Node root){
        if (root == null)
            return 0;
        if (root.left == null && root.right == null)
            return 1;
        else
            return numberLeafNodes(root.left) + numberLeafNodes(root.right);
    }



    int height() {
        return height(root);
    }

    private int height(Node node) {
        if (node == null)
            return 0;

        int leftHeight = height(node.left);
        int rightHeight = height(node.right);

        if (leftHeight > rightHeight)
            return (leftHeight + 1);
        else
            return (rightHeight + 1);
    }
}
