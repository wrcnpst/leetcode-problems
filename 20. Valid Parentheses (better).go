package main

func isValid(s string) bool {
    stack := make([]uint8, len(s))
    stackSize := -1

    for i := 0; i < len(s); i++ {
        switch s[i] {
            case '(','[','{':
                stackSize++
                stack[stackSize] = s[i]
            case ')', ']', '}':
                var openPar uint8
                switch s[i] {
                    case ')': openPar = '('
                    case ']': openPar = '['
                    case '}': openPar = '{'
                }
                if stackSize == -1 || stack[stackSize] != openPar {
                    return false
                } else {
                    stack[stackSize] = 0
                    stackSize--
                }
        }
    }

    return stackSize == -1
}
