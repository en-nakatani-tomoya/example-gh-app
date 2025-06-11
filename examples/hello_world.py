"""
A simple Hello World module for demonstration purposes.
"""

def say_hello(name="World"):
    """
    Returns a personalized hello message.
    
    Args:
        name (str): Name to personalize the greeting. Default is "World"
        
    Returns:
        str: Personalized greeting message
    """
    return f"Hello, {name}!"

def main():
    """
    Main function to demonstrate Hello World functionality.
    """
    print(say_hello())
    
if __name__ == "__main__":
    # Execute when the module is run directly
    main()