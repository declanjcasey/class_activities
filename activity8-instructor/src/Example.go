package main

import (
	"fmt"
	"math/rand"
)

var result bool
const MAX = 10

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func loop(total int, num float64) (string, float64) {
	for i := 0; i < total; i++ {
		num = num + float64(total)
	}
	return "finished", num
}

func main() {
	println("Hello World!");
	var num int
	num = 100

	print("Local var:", num, " and const", MAX, "\n")

	fmt.Println("Variables: ", num, " and ", MAX)
	fmt.Printf("Random number %d is generated\n", rand.Intn(100))
	fmt.Println(max(5, 10))
	fmt.Println(loop(10, 0.5))
}
