/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0; // Missing semicolon added
        }
        int lh = maxDepth(root.left);
        int rh = maxDepth(root.right);

        // Correct method call for finding the maximum using a reference to Math class
        return 1 + Math.max(lh, rh);
    }
}
