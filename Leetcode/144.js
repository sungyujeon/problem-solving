// Leetcode no.144 easy
// Binary Tree Preorder Traversal

var preorderTraversal = function(root) {
  
  const preorder = (node, res) => {
    if (!node) return
    
    preorder(node.left, res)
    preorder(node.right, res)
  }

  const res = []
  preorder(root, res)

  return res
};

const root = [1, null, 2, 3]
console.log(preorderTraversal(root))