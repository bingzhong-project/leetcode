public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) {
            return "";
        }
        String res = String.valueOf((char) root.val);
        if (root.left != null) {
            res += serialize(root.left);
        }
        if (root.right != null) {
            res += serialize(root.right);
        }
        return res;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == "") {
            return null;
        }
        char[] dataCharArray = data.toCharArray();
        int[] dataArray = new int[dataCharArray.length];
        for (int i = 0; i < dataCharArray.length; i++) {
            dataArray[i] = (int) dataCharArray[i];
        }

        return deserialize0(dataArray, 0, dataArray.length - 1);
    }

    private TreeNode deserialize0(int[] data, int start, int end) {
        if (start > end) {
            return null;
        }

        TreeNode root = new TreeNode(data[start]);
        int g = end + 1;
        for (int i = start + 1; i <= end; i++) {
            if (root.val < data[i]) {
                g = i;
                break;
            }
        }
        root.left = deserialize0(data, start + 1, g - 1);
        root.right = deserialize0(data, g, end);

        return root;
    }

    /**
     * Definition for a binary tree node.
     */
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }
}