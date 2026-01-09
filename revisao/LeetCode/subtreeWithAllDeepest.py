class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return 0, None
            
            depth_l, node_l = dfs(node.left)
            depth_r, node_r = dfs(node.right)
            
            if depth_l > depth_r:
                return depth_l + 1, node_l
            elif depth_r > depth_l:
                return depth_r + 1, node_r
            else:
                return depth_l + 1, node
        
        return dfs(root)[1]