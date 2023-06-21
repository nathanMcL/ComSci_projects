// Permutation formula: P(n,r) = n! ÷ (n-r)!
//combinations formula: _n C_r=\frac{n !}{r ! (n-r) !}

package main

import (
	"fmt"
)

// Main
// calculate the permutations of ___ and ___ (number of ways a particular set can be arranged)
func main() {
	permutations := factorial(13) / factorial(13-7)
	fmt.Println("The number of permutations of ___ and ___ is: ", permutations)

	// calculates the combinations of ___ and ___ ( number of ways a particular has combinations)
	combinations := factorial(13) / factorial(7) * factorial(13-7)
	fmt.Println("The number of combinations of ___ and ___ is", combinations)

}

// Factorial
func factorial(n int) int {
	if n == 0 {
		return 1
	} else {
		return n * factorial(n-1)
	}
}
