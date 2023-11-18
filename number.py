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
        return self.value % 2 == 1

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
        import math
        if self.value == 1:
            return False
        if self.value == 2:
            return True
        if self.value > 2 and self.value % 2 == 0:
            return False

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                divisors.append(i)
        return divisors   

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
        number_str = str(self.value)

        digit_sum = sum(int(digit) for digit in number_str)

        return digit_sum

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        reversed_number = int(str(self.value)[::-1])

        return reversed_number

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        number_str = str(self.value)
        return number_str == number_str[::-1]

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        number_str = str(self.value)
        digits = [int(digit) for digit in number_str]
        return digits

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        number_str = str(self.value)
        max_digit = max(int(digit) for digit in number_str)
        return max_digit

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        number_str = str(self.value)
        min_digit = min(int(digit) for digit in number_str)
        return min_digit

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        number_str = str(self.value)
        digits = [int(digit) for digit in number_str]
        average = sum(digits) / len(digits)

        return average


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
        number_str = str(self.value)

        digits = [int(digit) for digit in number_str]

        return range(min (digits),max(digits) +1)

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        number_str = str(self.value)

        # Initialize an empty dictionary to store digit frequencies
        frequency_dict = {}

        # Count the frequency of each digit
        for digit in number_str:
            # If the digit is already in the dictionary, increment its count
            if digit in frequency_dict:
                frequency_dict[digit] += 1
            # If the digit is not in the dictionary, add it with count 1
            else:
                frequency_dict[digit] = 1

        return frequency_dict
    

# Create a new instance of Number
number = Number(3)
