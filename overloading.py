# greeting.py

class Greeter:
    def greet(self, name=None):
        """Greets a person by name if provided, otherwise a general greeting"""
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello there!")

# Usage
g = Greeter()
g.greet()           # Output: Hello there!
g.greet("Alice")    # Output: Hello, Alice!
