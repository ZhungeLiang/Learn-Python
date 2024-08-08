# Input data

> # **Input data** : except user input <br>
> ## Syntax: variable_name = input("message")

<br><br>

> ## 1. Example : input basic info | basic output

```python
name = input("What is your name? : ")
age = input("How old are you? : ")
skill = input("what is your skill? : ")

print("Your name is " + name)
print("Your age is " + str(age) + " years old")
print("Your skill is " + skill)

```

<br><br>

> ## 2. Example : input basic info | dynamic output : all in single line with auto formatting data type

```python
name = input("What is your name? : ")
age = input("How old are you? : ")
skill = input("what is your skill? : ")

print("Your name is {:}".format(name))
print("Your age is {:} years old".format(age))
print("Your skill is {:}".format(skill))
```

<br><br>

> ## 3. Example : **type casting** for better readability | **Tip:** use "**\n**" to move to the next line

```python
username = str(input("Enter your username : "))
user_id = int(input("Enter your user ID : "))
user_height = float(input("Enter your user height : "))

print("Your username is " + username)
print("Your user ID is " + str(user_id))
print("Your user height is " + str(user_height) + " cm")

# or

print(("Your username is {:}\nYour user ID is {:}\nYour height is {:.2f} cm".format(username, user_id, user_height)))

# or

print(f"Username is {username}\nYour user ID is {user_id}\nYour height is {user_height} cm")
```