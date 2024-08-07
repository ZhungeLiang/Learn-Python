# Lesson 4 : String methods

> ## **String methods** has many different way to manipulate **string**

> ## Recommended download extension "**python snippets**" to preview all available features and functions

## Let's walk through each one

> 1. Example : **len()** | Count how many index of the string

```python
name = "Tony Stark" 
print(len(name))
# output: 10
```

> 2. Example : **find()** | Find where "string" is located as index

```python
name = "Steve Rogers"
print(name.find("S"))  # 0
print(name.find("e"))  # 2
print(name.find(" "))  # 5
print(name.find("g"))  # 8

```

> 3. Example : **capitalize()** | Capitalize the 1st index
```python
name = "bruce banner"
print(name.capitalize())
# output: Bruce banner
```

> 4. Example : **upper()** | Make every letter uppercase
```python
name = "John Wick"
print(name.upper())
# output: JOHN WICK
```

> 5. Example : **lower()** | Make every letter lowercase
```python
name = "JoHN wIcK"
print(name.lower())
# output: john wick
```

> 6. Example : **isdigit()** | Check condition if it a number(int/float) returns **True**, If not returns **False** | [**Note**] : This function has no effect on **int** and **float**

```python
name = "Vision"
user_id = "15"
print(name.isdigit())     # False
print(user_id.isdigit())  # True
```

> 7. Example : **isalpha()** | Check condition if it a string returns **True**, If not returns **False** | [**Note**] : This function has no effect on **int** and **float**

```python
name = "Thor"
age = "1500"
print(name.isalpha())  # True
print(age.isalpha())   # False
```

> 8. Example : **count()** | Count how many the same characters in a **string**

```python
name = "Peter Quill"
print(name.count("e"))  # 2
print(name.count("l"))  # 2
```

> 9. Example : **replace()** | Replace the selected character to the new character | Syntax .replace("selected character", "New character")

```python
name = "Thanos"
print(name.replace("s", "k"))
# output: Thanok

username = "Groot"
print(username.replace("o", "e"))
# output: Greet
```

> 10. Example : **Print the same string multiple times** | Syntax **print(variable*amount)**

```python
name = "Natasha"
print(name*5)
# output: NatashaNatashaNatashaNatashaNatasha
```

> # There are more useful "string methods". If you wish to learn more check out website ![]()