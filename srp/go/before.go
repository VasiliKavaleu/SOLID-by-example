package main

import (
	"fmt"
	"math"
)

type circle struct {
	radius float64
}

func (c circle) area() {
	fmt.Printf("circle area: %f\n", math.Pi * c.radius * c.radius) // simple method try to do 2 things: output result and culculate area
}

type square struct {
	length float64
}

func (s square) area() {
	fmt.Printf("square area: %f\n", s.length * s.length)
}

func main() {
	c := circle{radius: 5}
	c.area()

	s := square{length: 7}
	s.area()
}
