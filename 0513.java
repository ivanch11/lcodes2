/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        TreeNode node = null;
        while(!q.isEmpty()){
            node = q.poll();
            if (node.right!=null) q.add(node.right);
            if (node.left !=null) q.add(node.left);
        }
        return node.val;
    }
}