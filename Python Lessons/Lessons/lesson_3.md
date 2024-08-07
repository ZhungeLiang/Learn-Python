# Lesson 3 : Variable

> ## - **Variable** in Python is Dynamic which mean you can add raw variable and asign it with value. <br><br> - Your **Variable** will auto-detect your value wether it a **str**, **int**, **float** or **boolean** <br><br> - **[!]Remember[!]** your variable name must be **unique** to avoid getting the same name and enhance readability

## Example : basic **variable** & **print()**

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

> ## You can combine multiple variable or text in a single print() by using **"+"** sign <br><br> [!]Remember[!] You can only combine if all variable or text are **"string"** <br> [!] You cannot combine **string** with **number** or **boolean**

## Example : You can shorten output into 1 **print()**

```python
username = "Loki"
food = "pizza"

# Tip : Us empty string " " for spacing between character
print(username + " like " + food)
print(usernaem + " doesn't like " + food + " but he likes sandwich.")
```

> ## You can check your variable type to see if your variable store value as **str**, **int**, **flaot** or **boolean**

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