# A dictionary stores data in key-value pairs.

# Creating a dictionary

a = {"name": "John", "age": 30, "city": "New York"}
b = {1: "apple", 2: "banana", 3: "cherry"}
c = {"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", "coding", "traveling"]}
print(a, b, c,)

# Output

# {'name': 'John', 'age': 30, 'city': 'New York'} {1: 'apple', 2: 'banana', 3: 'cherry'} {'name': 'John', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'coding', 'traveling']}

# In the above example, a, b, and c are dictionary variables. a is {'name': 'John', 'age': 30, 'city': 'New York'}, b is {1: 'apple', 2: 'banana', 3: 'cherry'}, and c is {'name': 'John', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'coding', 'traveling']}.
# Accessing elements in a dictionary
# You can access elements in a dictionary by using their keys.

# Accessing elements in a dictionary

a = {"name": "John", "age": 30, "city": "New York"}
print(a["name"])
print(a["age"])
print(a["city"])

# Output

# John
# 30
# New York

# In the above example, we accessed the values of the keys "name", "age", and "city" in the dictionary a.