// Leetcode no.48 medium
// Rotate Image

var rotate = function(matrix) {
  const n = matrix.length
  const r_matrix = Array.from(Array(n), () => new Array(n));
  
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const k = n - j - 1
      r_matrix[i][k] = matrix[j][i]
    }
  }
  matrix = r_matrix
};

const matrix = [[1,2,3],[4,5,6],[7,8,9]]
console.log(rotate(matrix))