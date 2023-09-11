//
//  main.swift
//  Algorithm
//
//  Created by 최지철 on 2023/08/31.
//

import Foundation

let inputcount:Int = Int(readLine()!)!
var stack: [Int] = []

for _ in 0..<inputcount {
    let input = readLine()!.split(separator: " ").map { Int($0)! }

    let command = input.first!
    switch command {
    case 1:
        let result = input.last!
        stack.append(result)
    case 2:
        print(stack.popLast() ?? -1)
    case 3:
        print(stack.count)
    case 4:
        print(stack.isEmpty ? 1: 0)
    case 5:
        print(stack.last ?? -1)
    default:
        fatalError()
    }
}
