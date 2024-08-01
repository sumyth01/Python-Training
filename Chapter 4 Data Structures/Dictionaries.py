

# Dictionaries are unordered collections of key-value pairs.



# dict_name = {"key1": value1, "key2": value2}


# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: John

# Adding key-value pairs
person["email"] = "john@example.com"

# Removing key-value pairs
del person["age"]

# Looping through a dictionary
for key, value in person.items():
    print(key, value)
