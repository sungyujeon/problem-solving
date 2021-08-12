// 백준 19583번 S2
// 싸이버개강총회

const fs = require('fs')
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n')

const input = (() => {
  let line = 0
  return () => stdin[line++]
})()

const toTime = (time) => {
  const t = time.split(':')
  const hour = +t[0]
  const minute = +t[1]
  
  return hour * 100 + minute
}

const handleIn = (pm, name) => {
  if (!pm.has(name)) {
    pm.set(name)
  }
}

const isParticipated = (pm, name) => {
  if (pm.has(name)) {
    pm.delete(name)
    return 1
  }
  return 0
}

let res = 0
const participants_map = new Map()
const times_input = input().split(' ')
const [S, E, Q] = times_input.map(toTime)

while (true) {
  const participant_info = input()
  if (!participant_info) break

  const [t, name] = participant_info.split(' ')
  const time = toTime(t)

  if (time <= S) {
    handleIn(participants_map, name)
  } 

  if (E <= time && time <= Q) {
    res += isParticipated(participants_map, name)
  }
}

console.log(res)