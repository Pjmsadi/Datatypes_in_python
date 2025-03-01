# A set is an unordered collection that does not allow duplicate values.

# Creating a set

a = {1, 2, 3}
b = {"apple", "banana", "cherry"}
c = {1, "hello", 3.14}

print(a, b, c)

# Output

# {1, 2, 3} {'banana', 'apple', 'cherry'} {1, 'hello', 3.14}

# In the above example, a, b, and c are set variables. a is {1, 2, 3}, b is {'apple', 'banana', 'cherry'}, and c is {1, 'hello', 3.14}.
# Accessing elements in a set
# You cannot access elements in a set by using their index because sets are unordered. However, you can loop through the set to access its elements.
# Adding elements to a set
# You can add elements to a set using the add() method.

# Adding elements to a set

a = {1, 2, 3}
a.add(4)
print(a)

# Output

# {1, 2, 3, 4}
# In the above example, we added the element 4 to the set a using the add() method.
# Removing elements from a set
# You can remove elements from a set using the remove() method.

# Removing elements from a set

a = {1, 2, 3}
a.remove(2)
print(a)

# Output

# {1, 3}
# In the above example, we removed the element 2 from the set a using the remove() method.
# Set operations
# You can perform various set operations such as union, intersection, difference, and symmetric difference on sets in Python.