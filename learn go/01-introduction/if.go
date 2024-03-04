package main

import (
	"fmt"
	"math"
)

func main() {
	if v := math.Pow(10, 2); v > 10 {
		fmt.Print("more")
	} else {
		fmt.Print("less")
	}
}