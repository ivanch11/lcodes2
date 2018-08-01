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
    public int rob(TreeNode root) {
        return dp(root, new HashMap<>());
    }
    
    private int dp(TreeNode root, HashMap<TreeNode, Integer> map){
        if (root == null)
            return 0;
        if (map.containsKey(root))
            return map.get(root);
        int keep_root_val = root.val;
        if (root.left != null)
            keep_root_val += dp(root.left.left, map) + dp(root.left.right, map);
        if (root.right != null)
            keep_root_val += dp(root.right.left, map) + dp(root.right.right, map);
        int val = Math.max(keep_root_val,  dp(root.left, map) + dp(root.right, map) );
        map.put(root, val);
        return val;
    }
}