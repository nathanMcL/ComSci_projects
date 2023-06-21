package main

import (
	"fmt"
)

// Main
func main() {
	// Define the array numerical size
	numbers := []int{2, 3, 5, 7, 11, 13, 17}

	// Calculate the sum of the numbers
	sum := 0
	for _, number := range numbers {
		sum += number
	}

	// Calculate the average of the array of numbers
	average := sum / len(numbers)

	fmt.Println("The average of the numbers is: ", average)

}
