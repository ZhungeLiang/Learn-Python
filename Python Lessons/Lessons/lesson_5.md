# Type casting

> ## **Type casting** Use to change existed data types to another data type.
> ## Casting data types : **str** , **int** , **float** , **bool**

> 1. Example : Convert number inside a string into a **string** to join sentence. <br>
> **Python** won't join the sentence unless all data types are the same. In this case **str** + **str**.

```python
name = "Loki"
user_id = "50"
print(name + " " + str(user_id))
#output: Loki 50
```

> 2. Example : Assign data type to value

```python
x = 1
y = 2.0
z = "3"

x = float(x)
y = str(y)
z = int(z)
# or
print(float(x))
print(str(y))
print(int(z * 3))

#output:
# 1.0
# 2.0
# 9
```