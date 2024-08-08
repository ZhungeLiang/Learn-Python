# Lesson 4 : String methods

> ## **String methods** has many different way to manipulate **string**
> ## Recommended download extension "**python snippets**" to preview all available features and functions
> ## Let's walk through each one

<br><br>

> ## 1. **len()** | Count how many index of the string

<br>

```python
name = "Tony Stark" 
print(len(name))
# output: 10
```

<br><br>

> ## 2. **find()** | Find where "string" is located as index

<br>

```python
name = "Steve Rogers"
print(name.find("S"))  # 0
print(name.find("e"))  # 2
print(name.find(" "))  # 5
print(name.find("g"))  # 8

```

<br><br>

> ## 3. **capitalize()** | Capitalize the 1st index

<br>

```python
name = "bruce banner"
print(name.capitalize())
# output: Bruce banner
```

<br><br>

> ## 4. **upper()** | Make every letter uppercase

<br>

```python
name = "John Wick"
print(name.upper())
# output: JOHN WICK
```

<br><br>

> ## 5. **lower()** | Make every letter lowercase
```python
name = "JoHN wIcK"
print(name.lower())
# output: john wick
```

<br><br>

> ## 6. **isdigit()** | Check condition if it a number(int/float) returns **True**, If not returns **False** | [**Note**] : This function has no effect on **int** and **float**

<br>

```python
name = "Vision"
user_id = "15"
print(name.isdigit())     # False
print(user_id.isdigit())  # True
```

<br><br>

> ## 7. **isalpha()** | Check condition if it a string returns **True**, If not returns **False** | [**Note**] : This function has no effect on **int** and **float**

<br>

```python
name = "Thor"
age = "1500"
print(name.isalpha())  # True
print(age.isalpha())   # False
```

<br><br>

> ## 8. **count()** | Count how many the same characters in a **string**

<br>

```python
name = "Peter Quill"
print(name.count("e"))  # 2
print(name.count("l"))  # 2
```

<br><br>

> ## 9. **replace()** | Replace the selected character to the new character | Syntax .replace("selected character", "New character")

<br>

```python
name = "Thanos"
print(name.replace("s", "k"))
# output: Thanok

username = "Groot"
print(username.replace("o", "e"))
# output: Greet
```

<br><br>

> ## [**Tips & Tricks**] : Print the same string multiple times | Syntax: **print(variable*amount)**

<br>

```python
name = "Natasha"
print(name*5)
# output: NatashaNatashaNatashaNatashaNatasha
```

<br><br>

> ## 👉 There are more useful "string methods". If you wish to learn more check out website ![]()