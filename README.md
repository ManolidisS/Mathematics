# Mathematics Library
## Modules
To do basic mathematical operations in Python, you can either use the built-in operands `+`, `-`, `*`, `/`, `%`, `^`, `**`, etc., or you can use the `math` library, also directly built-in Python.
But what if you wanted to compute the dot product of a matrix? What if you wanted to calculate binomials?
There is probably some boring, ultra-efficient method on Stack Overflow 🥱, or instead you can use **my** incredible mathematics library (which is probably very efficient).

Honestly idk this is just a project for fun, but I might use it one day :)

## Flower.py
I was going over the basics of Python (because my school was forcing me to), and one of the tasks was to make a flower.
So obviously I devoted an entire evening to making it nice and pretty (sweat ik).
### How?
Basically I thought what if we take a quadratic graph `f(x) = x**2`, with restrictions `0 ≤ x ≤ 1`, it forms a nice curve.
If we find a way to do this curve, and then rotate 180deg, and do it again, we'd have a nice petal.

The way I did this was by using the *derivative* 🎉, specifically, using the tangent line formula and a for loop to create n tangent lines of the graph, then using a bit of trig to find the angles to turn.
