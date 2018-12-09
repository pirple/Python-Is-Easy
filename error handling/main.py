##
# Error Handling Lecture
##


# float("123.4") - > 123.4
# float("N/A") - > error

"""
'try' 'except' is a way of handling errors in phyton
Its similiar to if else block the difference being that if any errors occur in the 'try' block , the 'expect' block will be called automatically
"""


try:
    # Printing 'Hello' using the 'print()' function
    print("Hello")
except:
    # Printing 'Enterted Exception' only if any errors occur in the try block using the 'print()' function
    print("Entered exception")

# Output
"""
Hello
"""
# Hello is printed since no error occured in the try block


try:
    # Printing 'Hello' using the 'print()' function
    print(int("Hello"))
except:
    # Printing 'Enterted Exception' only if any errors occur in the try block using the 'print()' function
    print("Entered exception")

# Output
"""
Entered exception
"""
# Entered exception is printed since error occured in the try block



try:
    # Printing 'Hello' using the 'print()' function
    print(int("Hello"))
except:
    # Printing 'Enterted Exception' only if any errors occur in the try block using the 'print()' function
    print("Entered exception")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
Entered exception
Past exception
"""
# Both the Entered exception and passed exception has been printed , this shows that the program doesnt stops if an error has occured

# Declared a variable 'keyword' with a value of "123"
keyword="123"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
except:
    # Printing 'Enterted Exception' only if any errors occur in the try block using the 'print()' function
    print("Entered exception")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
123
Past exception
"""



# Declared a variable 'keyword' with a value of "Hello"
keyword="Hello"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
except:
    # Printing 'Enterted Exception' only if any errors occur in the try block using the 'print()' function
    print("Entered exception")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
Entered exception
Past exception
"""


# Declared a variable 'keyword' with a value of "Hello"
keyword="Hello"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
except:
    # The pass keyword is used to indicate when no operation needs to be done in the block , this is also used to move the execution forward
    pass

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
Past exception
"""


# Declared a variable 'keyword' with a value of "Hello"
keyword="Hello"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
except:
    # The pass keyword is used to indicate when no operation needs to be done in the block , this is also used to move the execution forward
    pass
    # Printing 'Enterted Exception' only if any errors occur in the try block using the 'print()' function
    print("Entered exception")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
Entered exception
Past exception
"""
# Both the Entered exception and Past exception has been printed , because 'pass' keyword is doesnt work like 'break'




# Declared a variable 'keyword' with a value of "Hello"
keyword="Hello"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
except Exception as e:
    # Printing the string version of the catched exception , The exception that has occured can be caught and stored in a variable
    print(str(e))

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
invalid literal for int() with base 10: 'Hello'
Past exception
"""


# Declared a variable 'keyword' with a value of "Hello"
keyword="Hello"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
# If known a specific error can be caught using the 'except' keyword
except ValueError:
    # Pinting "got a ValueError" using 'print()' function
    print("got a ValueError")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
got a ValueError
Past exception
"""


# Declared a variable 'keyword' with a value of "Hello"
keyword="Hello"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
# If known a specific error can be caught using the 'except' keyword
except ValueError:
    # Printing "got a ValueError" using 'print()' function
    print("got a ValueError")
# except can be chained together like if elif statements
except:
    # Printing "Other types of exception" using 'print()' function
    print("Other tpyes of exception")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
got a ValueError
Past exception
"""
# Since ValueError has occured only the 'except' block with 'ValueError' has been executed


# Declared a variable 'keyword' with a value of "Hello"
keyword="Hello"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
# If known a specific error can be caught using the 'except' keyword
except ValueError:
    # Printing "got a ValueError" using 'print()' function
    print("got a ValueError")
# except can be chained together like if elif statements
except:
    # Printing "Other types of exception" using 'print()' function
    print("Other tpyes of exception")
# The 'finally' block is a block always executed , no matter what happens in the 'try' 'except' block
finally:
    # Printing "finally" using 'print()' function
    print("finally")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
got a ValueError
finally
Past exception
"""
# finally has also printed because it always executed



try:
    # We can 'raise' call an error using the raise keyword even though the error doesnt occur in the program
    raise ValueError
# If known a specific error can be caught using the 'except' keyword
except ValueError:
    # Printing "got a ValueError" using 'print()' function
    print("got a ValueError")
# except can be chained together like if elif statements
except:
    # Printing "Other types of exception" using 'print()' function
    print("Other tpyes of exception")
# The 'finally' block is a block always executed , no matter what happens in the 'try' 'except' block
finally:
    # Printing "finally" using 'print()' function
    print("finally")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
got a ValueError
finally
Past exception
"""
# got a ValueError is printed because we rasied that error ourselves



try:
    # We can 'raise' call an error using the raise keyword even though the error doesnt occur in the program
    raise NameError
# If known a specific error can be caught using the 'except' keyword
except ValueError:
    # Printing "got a ValueError" using 'print()' function
    print("got a ValueError")
# except can be chained together like if elif statements
except:
    # Printing "Other types of exception" using 'print()' function
    print("Other tpyes of exception")
# The 'finally' block is a block always executed , no matter what happens in the 'try' 'except' block
finally:
    # Printing "finally" using 'print()' function
    print("finally")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
Other types of exception
finally
Past exception
"""
# Notice how "Other types of exception" is printed because we have not caught the 'NameError' in any 'except' block





try:
    # We can 'raise' call an error using the raise keyword even though the error doesnt occur in the program
    raise NameError
# If known a specific error can be caught using the 'except' keyword
except ValueError:
    # Printing "got a ValueError" using 'print()' function
    print("got a ValueError")
# except can be chained together like if elif statements
except:
    # Printing "Other types of exception" using 'print()' function
    print("Other tpyes of exception")
    # We can raise the same error again to manually crash the program
    raise
# The 'finally' block is a block always executed , no matter what happens in the 'try' 'except' block
finally:
    # Printing "finally" using 'print()' function
    print("finally")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
raise NameError
NameError
"""



try:
    # We can 'raise' call an error using the raise keyword even though the error doesnt occur in the program
    # A message of "Error" has been passed when we 'raise' the error
    raise NameError("Error")
# If known a specific error can be caught using the 'except' keyword
except ValueError:
    # Printing "got a ValueError" using 'print()' function
    print("got a ValueError")
# except can be chained together like if elif statements
# The error has been catched here and renamed it to 'e'
except Exception as e:
    # Printing "Other types of exception" using 'print()' function
    print("Other tpyes of exception")
    # Printing the String version of error 'e' using 'print()' function
    print(str(e))
# The 'finally' block is a block always executed , no matter what happens in the 'try' 'except' block
finally:
    # Printing "finally" using 'print()' function
    print("finally")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
Other tpyes of exception
Error
finally
Past exception
"""
# Notice the message "Error" has also been printed


# Declared a variable 'keyword' with a value of "Hello"
keyword="Hello"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
    # We can 'raise' call an error using the raise keyword even though the error doesnt occur in the program
    # A message of "Error" has been passed when we 'raise' the error
    raise NameError("Error")
# The error has been catched here and renamed it to 'e'
except Exception as e:
    # Printing "Other types of exception" using 'print()' function
    print("Other tpyes of exception")
    # Printing the String version of error 'e' using 'print()' function
    print(str(e))
# The 'finally' block is a block always executed , no matter what happens in the 'try' 'except' block
finally:
    # Printing "finally" using 'print()' function
    print("finally")

# Printing 'Past exception' using the 'print()' function
print("Past exception")
# Output
"""
Other tpyes of exception
invalid literal for int() with base 10: 'Hello'
finally
Past exception
"""
# Notice the message "Error" has also been printed
