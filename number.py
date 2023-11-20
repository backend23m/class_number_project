from math import sqrt

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
        return self.value % 2

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
        for i in range(2, int(sqrt(self.value)+1)):
            if self.value % i == 0:
                return False
        return True
    
    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors = [1, self.value]
        for i in range(2, int(sqrt(self.value)) + 1):
            if self.value % i == 0:
                divisors.append(i)
        return sorted(divisors)

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
        numbers = [int(i) for i in str(self.value)]
        return sum(numbers)

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.value)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        if self.get_length()%2:
            return self.value == self.get_reverse()

        return False

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return [int(i) for i in str(self.value)]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        return max(self.get_digits())

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        return min(self.get_digits())

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        return self.get_sum() / self.get_length() 

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        length = self.get_length()
        h_len = length//2
        s_number = str(self.value)

        if length % 2:
            return float((s_number)[h_len])

        return (float(s_number[h_len]) + float(s_number[h_len - 1])) / 2

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        return [list(range(i+1)) for i in self.get_digits()]

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        
        numbers = self.get_digits()
        l = list(set(numbers))
        dct = {}

        for key in l:
            dct[key] = numbers.count(key)

        return dct