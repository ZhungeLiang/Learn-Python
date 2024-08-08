# Math functions

> * ## Useful **math functions** will be vulnerable during complex calculations.
> * ## There are multiple **math functions**, let's walk through each one.

<br><br>

> # 1. round() = Will round up decimal numbers to the nearest integer.
> ## 0.49 or lower will round up to the lowerest integer.
> ## 0.50 or higher will round up to the highest integer.

* ## Example: PI = 3.14 will round up to 3 because ".14" is lower than 0.5 and 3 is the nearest integer.

```python
PI = 3.14
print(round(PI))
#output: 3
```

> # 2. **ceil()** = Will round up to the highest integer even if the decimal is lower than 0.5

* ## Example: PI = 3.14 will round up to 4 because 4 come after 3

```python
PI = 3.14
print(ceil(PI))
#output: 4
```

> # 3. **floor()** = Will round up to the lowest integer even if the decimal is grater than 0.5

* ## Example: PI = 3.14 will round up to 3 because 3 is the lowest integer

```python
PI = 3.14
print(floor(PI))
#output: 3
```

> ## 4. **abs()** = "absolutely" Will turn negative number into positive number.

* ## Example: X = -420.69 will turn into 420.69

```python
x = -420.69
print(abs(x))
#output: 420.69
```

> ## 5. **pow()** = Raise the power of number. Example: 2^5 = 2 * 2 * 2 * 2 * 2 = 32
> ## Syntax: pow(base, power)

* ## Example: PI^2 = ?, PI^5 = ?

```python
PI = 3.14
print(pow(PI, 2)) # PI * PI 2 times
#output: 9.8596

print(pow(Pi, 5)) # PI * PI 5 times
#output: 305.2447761824001
```

* ### **Pro tip:** Take 2 decimal of the power of number | Require "import math" function. <Br> We will discuss this later so that's okey if you don't understand.

```python
import math

pi_power_5 = math.pi ** 5
result = round(pi_power_5, 2)
print(result)

#output: 306.02
```

> ## 6. **sqrt()** = Require "**import math**" to work | **sqrt** = square root.
> ## [!]Remember[!] You cannot use square root as negative numbers.
> ## Syntax: math.sqrt()

* ## Exmaple: square root of PI | square root of random number

```python
import math

PI = 3.14
x = 25
y = 144

print(math.sqrt(PI))  # output: 1.772004514666935
print(math.sqrt(x))   # output: 5.0
print(math.sqrt(y))   # output: 12.0
```

> ## 7. **max()** = Find the highest/largest number of multiple values.
> ## [**Note**]: This will output only 1 value.

* ## Example: Let's create x, y, z = 100, 400, 250 and see which is the largest of all.

```python
x, y, z = 100, 400, 250
print(max(x, y, z))
# output: 400
```

> ## 8. **min()** = Find the lowest/smallest number of multiple values.
> ## [**Note**]: This will output only 1 value.

* ## Example: Let's create x, y, z = 600, 400, 20

```python
x, y, z = 600, 400, 20
print(min(x, y, z))
# output: 20
```

> *  ## These are useful **math function** in Python and use a lot in larger project.
> * ## There are other **math function** like **sin** , **cos** , **tan** , **log** , **log10** , **...**
> * ## Check out [hubspot](https://blog.hubspot.com/website/python-math-functions#dist) & [python library](https://docs.python.org/3/library/math.html) for more math function.