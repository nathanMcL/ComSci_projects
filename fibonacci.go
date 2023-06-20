package main

import "fmt"

func fibonacci(n int) int {
	if n == 0 {
		return 0
	}else if n == 1 {
		return 1
	}else {
		return fibonacci(n-1) + fibonacci(n-2)
	}
}

func main() {
	fmt.Println("The first ten Fibonacci numbers are:")
	for i := 0; i < 10; i++ {
		fmt.Println(fibonacci(i))
	}
}