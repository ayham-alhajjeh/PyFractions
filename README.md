# PyFractions

A simple Python project that implements a custom Fraction class.  
This class supports flexible initialization and string representation of fractions.

Features:-
  - Create fractions with:
    - (No Arguments) - defaults to 0/1
    - (One Argument) - sets numerator with denominator 1
    - (Two Arguments) - sets both numerator and denominator
  - Prevents division by zero errors
  - Simple string conversion using __str__


Example Usage:-

Create fractions:

a = Fraction()        # 0/1
b = Fraction(5)       # 5/1
c = Fraction(3, 4)    # 3/4

Display:

print(a)  # Output: 0/1
print(b)  # Output: 5/1
print(c)  # Output: 3/4


