import math
class Number:
    
    def __init__(self, value: int):
        self.value = value

    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value%2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return not self.is_odd()

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        lst = [1, self.value]
        for i in range(2, int(math.sqrt(self.value))+1):
            if self.value%i==0:
                lst.append(i)
        return len(lst)<3

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        i = 1
        l = []
        while i <= self.value:
            if self.value % i == 0:
                l.append(i)
                l.append(-i)
            i += 1
        return l
    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        list=[]
        list.append(self.value)
        return sum(list)

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return str(self.value)[::-1]

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        return self.value == str(self.value)[::-1]

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        pass

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        pass

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        pass

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        pass

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
v = Number(
    value = 20
)
print(v.get_number())
print(v.is_odd())
print(v.is_even())  
print(v.is_prime())
print(v.get_divisors())
print(v.get_length())
print(v.get_sum())
print(v.get_reverse())
print(v.is_palindrome())