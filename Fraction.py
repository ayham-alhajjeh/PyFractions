class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        if denominator == 0:
            raise ValueError("Denom can't be zero")
        
        
        self.numerator = numerator
        self.denominator = denominator
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
        


def main():
    a = Fraction() # str(a) returns "0/1"
    b = Fraction(5) # str(b)returns "5/1"
    c = Fraction(3,4) # str(c) returns "3/4"
    
    print(a)
    print(b)
    print(c)
    
main()