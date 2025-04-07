# Python Collections

Python provides several built-in collection types to store and organize data. Each type has unique properties and is suited for different use cases. Below is an overview of the main collection types in Python: **Lists**, **Tuples**, **Sets**, and **Dictionaries**.

---

## 1. Lists (`list`)

### Description
- A list is an **ordered** and **mutable** collection of elements.
- It allows duplicate elements and maintains the insertion order.

### Properties
- **Ordered**: Elements are stored in the order they were added.
- **Mutable**: You can modify, add, or remove elements after creation.
- **Allows duplicates**: The same value can appear multiple times.
- **Indexable**: Elements can be accessed by their index (zero-based).
- **Iterable**: Can be traversed using loops like `for`.

### Example
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
my_list.append(6)  # Adds an element to the end
print(my_list)     # Output: [1, 2, 3, 4, 5, 6]
```

### Common Use Cases
- Storing sequences of data that may change over time.

---

## 2. Tuples (`tuple`)

### Description
- A tuple is an **ordered** and **immutable** collection of elements.
- Once created, its elements cannot be changed, added, or removed.

### Properties
- **Ordered**: Elements maintain their insertion order.
- **Immutable**: Cannot be modified after creation.
- **Allows duplicates**: The same value can appear multiple times.
- **Indexable**: Elements can be accessed by their index (zero-based).
- **Iterable**: Can be traversed using loops like `for`.

### Example
```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
# my_tuple[0] = 10  # Error: Tuples are immutable
```

### Common Use Cases
- Storing fixed collections of items, such as coordinates or configuration values.

---

## 3. Sets (`set`)

### Description
- A set is an **unordered**, **mutable**, and **unique** collection of elements.
- It does not allow duplicate values.

### Properties
- **Unordered**: Elements do not have a specific order.
- **Mutable**: You can add or remove elements after creation.
- **No duplicates**: Each element in the set must be unique.
- **Not indexable**: Elements cannot be accessed by index.
- **Iterable**: Can be traversed using loops like `for`.

### Example
```python
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Adds an element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set.add(3)  # Attempt to add a duplicate
print(my_set)  # Output: {1, 2, 3, 4, 5, 6} (no duplicates)
```

### Common Use Cases
- Removing duplicates from a list.
- Performing mathematical set operations (union, intersection, difference, etc.).

---

## 4. Dictionaries (`dict`)

### Description
- A dictionary is an **unordered** collection of key-value pairs.
- Keys must be unique, but values can be duplicated.

### Properties
- **Unordered**: As of Python 3.7+, dictionaries preserve insertion order, but formally they are unordered.
- **Mutable**: You can add, modify, or remove key-value pairs.
- **Unique keys**: Each key must be unique, but values can repeat.
- **Access by key**: Values are accessed using their keys.
- **Iterable**: Can be traversed using loops like `for`.

### Example
```python
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict["name"])  # Output: John
my_dict["profession"] = "Engineer"  # Adds a new key-value pair
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'profession': 'Engineer'}
```

### Common Use Cases
- Storing data associated with specific keys, such as user information or configurations.

---

## Summary of Properties

| Collection Type | Ordered | Mutable | Allows Duplicates | Indexable | Iterable |
|------------------|---------|---------|-------------------|-----------|----------|
| **List**         | Yes     | Yes     | Yes               | Yes       | Yes      |
| **Tuple**        | Yes     | No      | Yes               | Yes       | Yes      |
| **Set**          | No      | Yes     | No                | No        | Yes      |
| **Dictionary**   | No      | Yes     | Keys no, values yes | By key | Yes      |

---

## Additional Collection Types (from `collections` Module)

Python's `collections` module provides specialized collection types for advanced use cases:

1. **`namedtuple`**:
   - A tuple with named fields.
   ```python
   from collections import namedtuple
   Point = namedtuple('Point', ['x', 'y'])
   p = Point(10, 20)
   print(p.x, p.y)  # Output: 10 20
   ```

2. **`deque`**:
   - A double-ended queue optimized for fast appends and pops from both ends.
   ```python
   from collections import deque
   queue = deque([1, 2, 3])
   queue.appendleft(0)  # Adds to the left
   print(queue)  # Output: deque([0, 1, 2, 3])
   ```

3. **`defaultdict`**:
   - A dictionary with default values for missing keys.
   ```python
   from collections import defaultdict
   d = defaultdict(int)
   d['key'] += 1
   print(d['key'])  # Output: 1
   ```

4. **`Counter`**:
   - A dictionary subclass for counting hashable objects.
   ```python
   from collections import Counter
   c = Counter(['a', 'b', 'a', 'c'])
   print(c)  # Output: Counter({'a': 2, 'b': 1, 'c': 1})
   ```

---

## Iterating Over Collections

### Using `for` Loop
You can iterate over any iterable collection using a `for` loop:
```python
my_list = [1, 2, 3]
for item in my_list:
    print(item)
```

### Using `while` Loop
For collections like sets, you can use a `while` loop with `.pop()` or convert the collection to a list:
```python
my_set = {1, 2, 3}
while my_set:
    item = my_set.pop()  # Removes and returns an arbitrary element
    print(item)
```

---

## Conclusion
Python provides four main built-in collection types: **lists**, **tuples**, **sets**, and **dictionaries**, each with unique properties. Additionally, the `collections` module offers specialized types for more advanced scenarios. Understanding these collections and their differences will help you write efficient and effective Python code.

---
