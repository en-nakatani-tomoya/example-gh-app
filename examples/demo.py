"""
Demo script showing how to use the hello_world module.
"""

# Import the say_hello function from the hello_world module
from hello_world import say_hello

def run_demo():
    # Print the default greeting
    print(say_hello())
    
    # Print a personalized greeting
    print(say_hello("Python User"))

if __name__ == "__main__":
    run_demo()