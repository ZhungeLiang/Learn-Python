# Lesson 3 : Variable

> ## - **Variable** in Python is Dynamic which mean you can add raw variable and asign it with value. <br><br> - Your **Variable** will auto-detect your value wether it a **str**, **int**, **float** or **boolean** <br><br> - **[!]Remember[!]** your variable name must be **unique** to avoid getting the same name and enhance readability

<br><br>

## Basic **variable** & **print()**

```python
name = "Thor Odinson"
age = 1500
balance = 97500.79
isAvenger = True

print(name)
print(age)
print(balance)
print(isAvenger)
```

<br><br>

> ## 1. You can combine multiple variable or text in a single print() by using **"+"** sign <br><br> [!]Remember[!] You can only combine if all variable or text are **"string"** <br> [!] You cannot combine **string** with **number** or **boolean**

<br>

## Example : You can shorten output into 1 **print()**

```python
username = "Loki"
food = "pizza"

# Tip : Us empty string " " for spacing between character
print(username + " like " + food)
print(usernaem + " doesn't like " + food + " but he likes sandwich.")
```

<br><br>

> ## 2. You can check your variable type to see if your variable store value as **str**, **int**, **flaot** or **boolean**

<br>

```python
villain = "Thanos"
army = 9999
height = 2.01
isHero = False

print(type(villain)) # str
print(type(army))    # int
print(type(height))  # float
print(type(isHero))  # boolean
```

<br><br>

> ## [**Tips & Tricks**] : You can declare multiple variables in a line

<br>

```python
x, y, z = 500, 700, 900
print(x, y, z)
# output: 500 700 900
```

<br><br>

> ## [**Tips & Tricks**] : Spacing methods using ( **^** , **<** , **>** )
> * ## Use **^** to add space both side. Ex: **{:^10}** space 5 times each side
> * ## Use **<** to add space to right side. Ex: **{:<10}** = space 10 times on right side
> * ## Use **>** to add space to left side. Ex: **{:>10}** = space 10 times on left side

<br>

```python
sale_week1, sale_week2, sale_week3 = 200, 250, 300

total_sale = sale_week1 + sale_week2 + sale_week3

# Use ^
print("Total sale of the week = {:^10} $".format(total_sale))
# output: Total sale of the week =    750     $

# Use <
print("Total sale of the week = {:<10} $".format(total_sale))
#output: Total sale of the week = 750        $

# Use >
print("Total sale of the week = {:>10} $".format(total_sale))
#output: Total sale of the week =        750 $
```
