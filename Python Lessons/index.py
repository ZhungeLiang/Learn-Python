## 3. Type casting: Convert the data type of a value to another data type

> ### To use type casting, just write **"data type"** and () <br> **int() <br> float() <br> str() <br> boolean()**

> Example : Let's try convert everything into string. Remember string can't calculate.

```python
    x = 1    #int
    y = 2.0  #float
    z = "3"  #str

    x = str(x)
    y = str(y)
    z = str(z)
    # This will convert anything inside () into str

    print(x)
    print(y)
    print(z)
```

> Example : let's try using all 4 data type plus combine str together

> We haven't discuss **"varviable"** yet so don't focus on it too much, we'll get into that later.

```python
    qty = 3
    price = 2.99
    customer = "Steven Strange"
    isAvenger = True
    islawyer = False

    # Use + sign to combine text into 1 sentence
    # You must convert your variable into 

    print("Barista:" + " How many cup of cafe would you like?")
    print(customer + ": " + str(qty) + " please.")
    print()
```