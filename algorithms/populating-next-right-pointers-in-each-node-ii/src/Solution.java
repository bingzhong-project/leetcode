/**
 * Definition for binary tree with next pointer.
 */
public class TreeLinkNode {
    int val;
    TreeLinkNode left, right, next;

    TreeLinkNode(int x) {
        val = x;
    }
}

public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) {
            return;
        }

        TreeLinkNode nextNode = root.next;
        while (nextNode != null) {
            if (nextNode.left != null) {
                nextNode = nextNode.left;
                break;
            }
            if (nextNode.right != null) {
                nextNode = nextNode.right;
                break;
            }
            nextNode = nextNode.next;
        }

        if (root.right != null) {
            root.right.next = nextNode;
        }

        if (root.left != null) {
            root.left.next = root.right == null ? nextNode : root.right;
        }

        connect(root.right);
        connect(root.left);
    }
}