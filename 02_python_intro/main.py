# typescript is superset of javascript are not compiled language
# Mojo is superset of python
# Python is an interpreter language

a = "Abdul Qadir" 
print(a)

b: str ="Abdul Qadir Samdani" 
        
print(b)

print(type(b))

print(id(b)) #physical address

#set
#A set is an unordered collection of unique elements. In Python, sets are defined using curly braces {} or the set() constructor.
my_set = {1, 2, 3}

#tuple
#A tuple is an ordered, immutable collection of elements. Tuples are defined using parentheses () or the tuple() constructor.
my_tuple = (1, 2, 3)

#dictionary
#A dictionary is an unordered collection of key-value pairs. Each key in a dictionary is unique and associated with a value. Dictionaries are defined using curly braces {} or the dict() constructor.
my_dict = {"name": "John",
                    "age": "30"}

#fstring used for concatenation
#An f-string, short for "formatted string," is a way to create strings in Python that can include values or expressions inside them. It allows you to embed variables or expressions directly within a string, making it easier to build strings dynamically.

name: str = "Alice"
age:int = 25

# Using an f-string to create a string with placeholders
message:str = f"My name is:\t {name}\n I am: \t{age} years old."
#message_2: str = "My name is"\t+name "and I am years old."

print(message)


c : str ='"pakistan zindabad" this is a famous slogan'
f : str ='line 1\
        line 2\
        line 3'
print(f)
print(c)

#concatenation
name_1:str = "Alice"
fname:str = "steward"
age_1:int = 25
edu:str="bscs"
card:str ="Piaic student card"