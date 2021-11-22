var deleteDuplicates = function(head) {
  const arr = []
  let curr = -101
  const n = head.length
  let i = 0
  while (head[i] < n) {
      const curr_val = head[i]
      if (curr_val !== curr) {
          arr.push(curr_val)   
      } 
    curr = head[i]
      i++
  }

  return arr
};

const arr = [1,1,2]
console.log(deleteDuplicates(arr))