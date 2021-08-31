function solution(price, money, count) {
  let answer = 0

  const total = price * (count * (count + 1) / 2)
	const remainder = total - money
  answer = remainder < 0 ? 0 : remainder

  return answer
}