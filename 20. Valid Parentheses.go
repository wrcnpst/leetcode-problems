package main

func checkMap(mapCheck map[string]string, c1 string, c2 string) bool {
    // fmt.Println("checking: ", c1, c2)
	if mapCheck[c1] == c2 {
		return true
	} else {
		return false
	}
}

func isValid(s string) bool {

    if len(s) % 2 != 0 {
        return false
    }

    mapCheck := map[string]string{
        "(": ")",
        "{": "}",
        "[": "]",
    }

    open := ""
    
	for i := 0; i < len(s); i += 1 {
        _, isOpen := mapCheck[string(s[i])]
        if isOpen {
            open += string(s[i])
        } else {
            if len(open) == 0 || !checkMap(mapCheck, open[len(open)-1:], string(s[i])){
                return false
            }
            open = open[:len(open)-1]
        }
        // fmt.Println("open: ", open)
	}

    if len(open) > 0 {
        return false
    }

	return true
}