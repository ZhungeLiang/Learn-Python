# Arithmetic operations

> ## **Arithmetic operations** = Operators use to calculate in mathematical.
> ## There are 7 operations: ( + , - , * , / , % , //, ** ) We'll walk through each one.

<br><br>

> ## 1. Arithmetic operations ( **+** ) : Simple addition.

<br>

## Example : x + y = ?

```python
x = 20
y = 5

print(x + y)
#or
z = x + y
print(z)
```

<br>

## **Tips** : Use **type casting** convert number as **str** to **int** or **float** to perform calculation.

```python
x = 10  # int
y = '5' # str
print(x + int(y))
```

```python
# When user input numebr as string
num1 = str(input("Enter 1st number: ")) # input: 3
num2 = str(input("Enter 2nd number: ")) # input: 1

print(int(num1 + num2))       # 31
print(int(num1) + int(num2))  # 4

# 1st print() = 31 because str + str so '3' + '1'
# 2nd print() = int + int = 3 + 1 = 4
```

<br><br>

> ## 2. Arithmetic operations ( **-** ) : Simple substraction.

## Example : x - y = ?

```python
x = 50
y = 20
z = x - y
print(z) # 30
```

## Example : input x and y

```python
num1 = input("Enter 1st number: ") # input: 20
num2 = input("Enter 2nd number: ") # input: 5

print(int(num1) - int(num2)) # 15
```

<br>

```python
num1 = int(input("Enter 1st number: ")) # input: 20
num2 = int(input("Enter 2nd number: ")) # input: 5

print(num1 - num2) # 15
```

<br><br>

> ## 3 Arithmetic operations ( * ) : Simple multiplication.

<br>

## Example : let's try float

```python
num1 = input("Enter 1st number: ") # input: 3.14
num2 = input("Enter 2nd number: ") # input: 2

print(float(num1) * float(num2))   # 6.28
```

<br><br>

> ## 4. Arithmetic operations ( **/** ) : Simple division.

<br>

## Example : Let's try float + take 2 decimal

```python
num1 = float(input("Enter 1st number: ")) # input: 3.14
num2 = float(input("Enter 2nd number: ")) # input: 2.1

result = num1 / num2

print(f"Result: {result:.2f}")  # Result: 1.50
# or
print("Result: {:.2f}".format(result))  # Result: 1.50
```

<br><br>

> ## 5.  Arithmetic operations ( **%** ) : "Modulus Operator" : Returns the remainder of a division operation.
> ## Similar to **/** but return the ***remainder*** instead of the actual result.

<br>

# Example : Basic division

```python
print(15 % 3)    # 0
print(20 % 2.5)  # 0.40000000000000124
print(25 % 4)    # 1
print(30 % 6.5)  # 3.719999999999999
```

<br>

## Example : Let's try input + take 3 decimal

```python
x = input("Enter 1st number: ")
y = input("Enter 2nd number: ")

result = float(x) % float(y)

print(f"Result =  {result:.3f}")  # Result = 0.250
# or
print("Result = {:.3f}".format(result)) # Result = 0.250
```


> ## 6. Arithmetic operations ( **//** ) : "Floor Division Operator" : Rounds a number to the nearest integer.

<br>

## Example : Let's try simple calculation

```python
print(5 // 3) # 1
# The actaul result = 1.666666667 but // will always round down to the nearest integer. 
```

## Example : Let's try input

```python
num1 = input("Enter 1st number: ") # input: 10
num2 = input("Enter 2nd number: ") # input: 3

result = int(num1) // int(num2)

# [Trick]: New style of output
print("Result: ", result) # 3
```

<br><br>

> ## 7. Arithmetic operations ( ** ) : "Double Asterisk" : Raise power of number.
> ## Syntax: x ** y = x^y

<br>

## Example : Let's try simple calcutation + take 2 decimal

```python
print(2 ** 3) # 2 * 2 * 2 = 8
print(5 ** 2) # 25
print(4 ** 4) # 256
```

<br>

## Example : Let's try input

```python
num1 = input("Enter 1st number: ") # input: 3.14
num2 = input("Enter 2nd number: ") # input: 4

result = float(num1) ** float(num2)

print("Result = {:.2f}".format(result)) # Result = 97.21
```