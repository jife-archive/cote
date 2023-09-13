import Foundation

let t = Int(readLine()!)!

var results: [Int] = []

for _ in 0..<t {
    let k = Int(readLine()!)!
    let fileSizes = readLine()!.split(separator: " ").map { Int($0)! }
    
    // 비용 계산을 위한 배열 초기화
    var costMatrix: [[Int]] = Array(repeating: Array(repeating: 0, count: k), count: k)
    
    for len in 2...k {
        for i in 0...(k - len) {
            let j = i + len - 1
            costMatrix[i][j] = Int.max
            for x in i..<j {
                costMatrix[i][j] = min(costMatrix[i][j], costMatrix[i][x] + costMatrix[x + 1][j])
            }
            costMatrix[i][j] += fileSizes[i...j].reduce(0, +)
        }
    }
    results.append(costMatrix[0][k - 1])
}

// 결과 출력
for result in results {
    print(result)
}
