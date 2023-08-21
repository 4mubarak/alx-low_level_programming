import ctypes

# Load the dynamic library
mylib = ctypes.CDLL('./mylib.so')  # Use './mylib.dll' on Windows

# Call the 'add' function from C
result = mylib.add(5, 3)
print(f"Result of adding: {result}")

# Call the 'greet' function from C
mylib.greet(b"Python")
