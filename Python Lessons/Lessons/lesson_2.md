# Lesson 2 : Output

## 1. Use **print("text")** to output any text or message you wish

<br><br>

> Try print **"Hello world"** and run

<br>

```python
print("Hello world")
```

<br><br>

> Let's print multiple line. How about you introduce yourself

<br>

```python
print("My name is John")
print("I am 20 years old")
print("I am a software engineer")
print("I like pizza")
print("My hobby are watching movies and play games")
```

<br><br>

## 2. In Python you can print different data type like 
* ## **int** for number
* ## **float** for decimal number
* ## **str** for text
* ## **bool** for True or False statement

<br><br>

> ## **int** : normal number. <br> Can't be decimal and will convert into the actual number.

<br>

## Example : Print some number

```python
print(-420)
print(69.9)  # output: 69
print(11.11) # output: 11
print(750)
```

<br><br>

> ## **float** : decimal number "12.34" <br> Will turn normal number 80 -> 80.0 or 80.00

<br>

## Example : Print some decimal number

```python
print(69.97)
print(3.14)
print(0.12)
print(50) # output: 50.00
```

<br><br>

> ## **str** : anything inside " " will count as letter and can't be calculated.

<br>

## Example : Print some text

```python
print("Hello there!")
print("Do you like pizza?")
print("Will you marry me?")
print("My bill this month: 780.9$")
```

<br><br>

> ## **bool** : can 2 answer, either True or False

<br>

## Example : Print **True** or **False**

```python 
print("I am Iron man")
print(False)
print("I am bad at math")
print(True)
```

<br><br>

> ## Use **.format()** or **f** to auto format the variable when output and to set decimal number

<br>

## Example : Print text along with variable value

```python
x = 20

print(f"I am {x} years old")
# or
print("I am {:} years old".format(x))
```

<br><br>

## Example : Print text with decimal number

```python
y = 3.14159
print("PI = {:.2f}".format(y)) # .2f = take only 2 decimal

z = 420.6912415
print("Z = {:.5f}".format(z)) # .5f = will take 5 decimal
```
