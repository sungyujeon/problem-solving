// 올리브영 기지국

// x, y max/min 각 -1

const isInBound = (xs, ys, rs, point) => {
  const [tx, ty] = point
  let flag = false

  for (let i = 0; i < xs.length; i++) {
    const [_x, _y, _r] = [xs[i], ys[i], rs[i]]
    const [l, r] = [_x - _r, _x + _r]
    const [b, t] = [_y - _r, _y + _r]
    
    if ((l < tx && tx < r && b < ty && ty < t)
      || ((tx === _x) && (ty === _y - _r || ty === _y + _r))
      || ((ty === _y) && (tx === _x - _r || tx === _x + _r))
    ) {
      flag = true
    }
  }
  return flag
}

const createRandomPoints = (v, square_info) => {
  const points = []
  for (let i = 0; i < v.length; i += 2) {
    const [x, y] = [v[i], v[i+1]]
    const [l, r, b, t] = square_info

    const point = [l + x % (r - l), b + y % (t-b)]
    points.push(point)
  }

  return points
}

const getSquare = (x, y, r) => {
  const xs = []
  const ys = []

  for (let i = 0; i < x.length; i++) {
    const _r = r[i]
    xs.push(x[i] + _r)
    xs.push(x[i] - _r)
    ys.push(y[i] + _r)
    ys.push(y[i] - _r)
  }

  const [min_x, max_x] = [Math.min(...xs), Math.max(...xs)]
  const [min_y, max_y] = [Math.min(...ys), Math.max(...ys)]
  
  return [min_x, max_x, min_y, max_y]
}

const solution = (x, y, r, v) => {
    let answer = 0
    
    let total = 0
    const square_info = getSquare(x, y, r)
    const points = createRandomPoints(v, square_info)

    for (const point of points) {
      if (isInBound(x, y, r, point)) {
        total++
      }
    }
    
    const k = total / points.length
    const [left, right, bottom, top] = square_info
    
    answer = k * ((right-left) * (top - bottom))
    
    return answer
}

const x = [5]
const y = [5]
const r = [5]
const v = [92, 83, 14, 45, 66, 37, 28, 9, 10, 81]
console.log(solution(x, y, r, v))